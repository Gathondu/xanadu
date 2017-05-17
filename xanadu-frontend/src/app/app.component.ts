import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { Subject } from 'rxjs/Subject';

import { DataService } from "../app/services/data.service";
import { AlertService } from "../app/services/alert.service";
import { UserService } from "../app/services/user.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  username: any;
  loggedIn = false;
  constructor(
    private _router: Router,
    private _alert: AlertService,
    private _user: UserService
    ) {
   }
  ngOnInit() {
    this._alert.getUsername().subscribe(
      data => {
      this.username = data;
      if (localStorage.getItem('verified') == 'true'){
        this.loggedIn = true;
      }else{
        this.loggedIn = false;
      }
    });
  }
}
