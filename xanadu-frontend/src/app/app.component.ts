import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { Subject } from 'rxjs/Subject';

import { DataService } from "../app/services/data.service";
import { AlertService } from "../app/services/alert.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  verified: boolean;
  username: any;
  title = 'Welcome to your Bucketlist App';
  showTitle: boolean = true;
  constructor(private _router: Router, private _alert: AlertService) {
   }
  ngOnInit() {
    setTimeout(function () { this.showTitle = false }.bind(this), 7500);
    this._alert.getUsername().subscribe(
      data => {
      this.username = data;
    });
  }
}
