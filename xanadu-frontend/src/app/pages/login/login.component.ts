import { Component, OnInit } from '@angular/core';
import {Http, RequestOptions, Response} from "@angular/http";
import {Observable} from "rxjs/Observable";
import {ActivatedRoute, Router} from "@angular/router";
import {AuthenticationService} from "../../services/authentication.service";
import {AlertService} from "../../services/alert.service";
import {CookieService} from "ng2-cookies";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [
    AuthenticationService,
    AlertService,
    CookieService
  ]
})
export class LoginComponent implements OnInit {

  model: any = {};
  loading = false;
  returnUrl: string;
  private _baseUrl = 'http://127.0.0.1:5000';


  constructor(
    private _route: ActivatedRoute,
    private _router: Router,
    private _auth: AuthenticationService,
    private _alert: AlertService
  ) { }

  ngOnInit() {
    // reset login status
    this._auth.logout();

    // get return url from route parameters or default to '/'
    this.returnUrl = this._route.snapshot.queryParams['returnUrl'] || '/';
  }

  login() {
    this.loading = true;
    this._auth.login(this.model.username, this.model.password)
      .subscribe(
        data => {
          console.log("ndio huyo mimi", this.returnUrl);
          this._router.navigate(['/bucketlist'])
            .then(() => {
            console.log('navigated');
            })
            .catch(err => {
              console.log('could not navigate', err);
            })
        },
        error => {
          this._alert.error(error);
          this.loading = false;
        }
      );
  }
}
