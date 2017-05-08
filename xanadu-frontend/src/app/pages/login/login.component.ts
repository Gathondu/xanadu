import { Component, OnInit } from '@angular/core';
import {Http, RequestOptions, Response} from "@angular/http";
import {Observable} from "rxjs/Observable";
import {ActivatedRoute, Router} from "@angular/router";

import { AlertService } from "../../services/alert.service";
import { UserService } from "../../services/user.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [
    UserService,
    AlertService
  ]
})
export class LoginComponent implements OnInit {

  model: any = {};
  loading = false;
  returnUrl: string;

  constructor(
    private _route: ActivatedRoute,
    private _router: Router,
    private _user: UserService,
    private _alert: AlertService
  ) { }

  ngOnInit() {
    this._user.logout();
    // get return url from route parameters or default to '/'
    this.returnUrl = this._route.snapshot.queryParams['returnUrl'] || '';
  }

  login() {
    this.loading = true;
    this._user.login(this.model.username, this.model.password)
      .subscribe(
        data => {
          this._router.navigate([this.returnUrl]);
            },
        error => {
          this._alert.error(error);
          this.loading = false;
        }
      );
  }
}
