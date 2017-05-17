import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  title = "welcome to your bucketlist app";
  showTitle = true;
  bucketlist = {};
  created = [];
  modified = [];
  completed = [];
  constructor(
    private _data: DataService,
    private _alert: AlertService
  ) { }

  ngOnInit() {
    setTimeout(function () { this.showTitle = false }.bind(this), 7500);
    this.getBucketlists();
  }

  getBucketlists() {
    // get bucketlist objects
    return this._data.get('/api/v1.0/bucketlist/')
      .subscribe(data => {
        this.bucketlist = data;
      },
      error => {
        this._alert.error(error);
      });
  }
}
