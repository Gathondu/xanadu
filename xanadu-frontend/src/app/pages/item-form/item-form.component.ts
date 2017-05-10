import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, Params } from "@angular/router";

import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";

@Component({
  selector: 'item-form',
  templateUrl: './item-form.component.html',
  styleUrls: ['./item-form.component.css']
})
export class ItemFormComponent implements OnInit {
  heading = 'Add Item';
  listId: number;
  itemId: number;
  model: any = {};
  constructor(
    private _data: DataService,
    private _alert: AlertService,
    private _router: Router,
    private _route: ActivatedRoute
  ) { }

  ngOnInit() {
    this.listId = this._route.snapshot.queryParams['id'] || ''
    this._route.queryParams.subscribe(
      (params: any) => {
        if (params['item']) {
          this.listId = JSON.parse(params.item)[0].list;
          this.itemId = JSON.parse(params.item)[1].id;
          this.model.title = JSON.parse(params.item)[2].title;
          this.model.body = JSON.parse(params.item)[3].body;
        }
      });
    if (this.itemId) {
      this.heading = 'Edit Item';
    }
  }
  addItem() {
    let body = { title: this.model.title, body: this.model.body };
    if (!this.itemId) {
      this._data.post('/api/v1.0/bucketlist/' + this.listId + '/items/', body)
        .subscribe(
        data => {
          this._alert.success('Item added', true);
          this._router.navigate(['/bucketlist/' + this.listId]);
        },
        error => {
          this._alert.error(error);
        }
        );
    } else {
      this._data.put('/api/v1.0/bucketlist/' + this.listId + '/items/' + this.itemId, body)
        .subscribe(
        data => {
          this._alert.success('Item updated successfully', true);
          this._router.navigate(['/bucketlist/' + this.listId + '/items/' + this.itemId]);
        },
        error => {
          this._alert.error(error);
        }
        );
    }
  }

}
