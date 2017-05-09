import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";

@Component({
  selector: 'bucketlists',
  templateUrl: './bucketlists.component.html',
  styleUrls: ['./bucketlists.component.css'],
})
export class BucketlistsComponent implements OnInit {
  title = `Welcome to your Bucketlist App`;
  username = `${localStorage.getItem('username')}`;

  errorMessage: string;
  bucketlist = {};
  constructor(
    private _dataService: DataService,
    private _alert: AlertService
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

}
