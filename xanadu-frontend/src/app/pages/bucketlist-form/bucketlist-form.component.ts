import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from "@angular/router";

import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";

@Component({
  selector: 'bucketlist-form',
  templateUrl: './bucketlist-form.component.html',
  styleUrls: ['./bucketlist-form.component.css']
})
export class BucketlistFormComponent implements OnInit {

  heading = 'Add Bucketlist';
  listId: number;
  model: any = {};
  submitted = false;
  constructor(
    private _data: DataService,
    private _alert: AlertService,
    private _router: Router,
    private _route: ActivatedRoute
  ) { }

  ngOnInit() {
    this.listId = Number(this._route.snapshot.params['id']);
    if (this.listId) {
      this.heading = 'Edit Bucketlist'
    }
  }
  onsubmit() { this.submitted = true; }

  addList() {
    let body = { title: this.model.title, description: this.model.description };
    if (!this.listId) {
      this._data.post('/api/v1.0/bucketlist/', body)
        .subscribe(
        data => {
          this._alert.success('Bucketlist added', true);
          this._router.navigate(['/bucketlist']);
        },
        error => {
          this._alert.error(error);
        }
        );
    }else{
      this._data.put('/api/v1.0/bucketlist/', body)
      .subscribe(
        data => {
          this._alert.success('Bucketlist updated successfully');
          this._router.navigate(['/bucketlist']);
        },
        error => {
          this._alert.error(error);
        }
      );
    }
  }

}
