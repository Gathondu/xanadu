import { Injectable } from '@angular/core';
import {Headers, Http, RequestOptions, Response} from "@angular/http";
import {Observable} from "rxjs/Observable";


import 'rxjs/add/operator/map'
import 'rxjs/add/operator/catch'



@Injectable()
export class AuthenticationService {

  private _baseUrl = 'http://127.0.0.1:5000';
  constructor(
    private _http: Http,
  ) {
  }
  createAuthorizationHeader(headers: Headers) {
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT');
    headers.append('Accept', 'application/json');
    headers.append('Authorization', 'Token ' + localStorage.getItem('token') );
  }

  login(username: string, password: string){
    let body = JSON.stringify({username: username, password: password});
    let options = new RequestOptions(new Headers({'Content-Type': 'application/json'}));
    return this._http.post(`${this._baseUrl}/auth/login`, body, options)
      .map(this.extractData)
      .catch(this.handleError);
  }

  logout() {
    //remove token from cookie
    localStorage.removeItem('token');
  }

  private extractData(response: Response) {
    let body = response.json();
    // login successful if there is a token
    if (body.token) {
      // store details of the user in local storage
      console.log('hapa', body.token);
      localStorage.setItem('token', body.token);
      console.log('this', localStorage.getItem('token'));
    }
    return body || { };
  }

  private handleError(error: Response | any){
    let errMsg: string;
    if (error instanceof Response){
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    }else {

      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg)
  }
}
