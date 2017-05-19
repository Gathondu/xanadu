import { Injectable } from '@angular/core';
import {Headers, Http, RequestMethod, RequestOptions, Response} from "@angular/http";
import {Observable} from "rxjs/Rx";


import 'rxjs/add/operator/map'
import 'rxjs/add/operator/catch'



@Injectable()
export class AuthenticationService {

  private _baseUrl = 'http://127.0.0.1:5000';
  constructor(
    private _http: Http,
  ) {
  }
}
