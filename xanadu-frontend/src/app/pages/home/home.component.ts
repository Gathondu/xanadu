import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";
import { AppComponent } from "../../app.component";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  title = "welcome to your bucketlist app";
  showTitle = true;
  loggedIn = false;
  bucketlist = {};
  created = [];
  modified = [];
  completed = [];
  constructor(
    private _data: DataService,
    private _alert: AlertService,
    private _app: AppComponent
  ) { }

  ngOnInit() {
    setTimeout(function () { this.showTitle = false }.bind(this), 7500);
    this.loggedIn = this._app.loggedIn;
  }
}
