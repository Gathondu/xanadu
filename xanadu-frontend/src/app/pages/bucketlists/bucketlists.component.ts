import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";
import { Router } from "@angular/router";

@Component({
  selector: 'bucketlists',
  templateUrl: './bucketlists.component.html',
  styleUrls: ['./bucketlists.component.css'],
})
export class BucketlistsComponent implements OnInit {
  title = 'Welcome to your Bucketlist App';

  errorMessage: string;
  bucketlist = {};
  constructor(
    private _dataService: DataService,
    private _alert: AlertService,
    private _route: Router
  ) { }

  ngOnInit() {
    this.getBucketList();
  }

  getBucketList() {
    // get bucketlist objects
    return this._dataService.get('/api/v1.0/bucketlist/')
      .subscribe(data => {
        this.bucketlist = data;
      },
      error => {
        this._alert.error(error);
      });
  }

  removeList(id) {
    this._dataService.delete('/api/v1.0/bucketlist/' + id)
      .subscribe(
      data => {
        this._alert.success('Bucketlist Deleted');
        this.getBucketList();
      },
      error => {
        this._alert.error(error);
      }
      );
  }

}
