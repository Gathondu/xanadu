import { Injectable } from '@angular/core';
import { AuthenticationService } from "app/services/authentication.service";
import { RequestOptions, Http, Response, Headers } from "@angular/http";
import { Observable } from "rxjs/Rx";

@Injectable()
export class UserService {

  private _baseUrl = 'http://127.0.0.1:5000';
  constructor(
    private _http: Http,
  ) { }

  login(username: string, password: string) {
    let body = { username: username, password: password };
    let options = new RequestOptions(new Headers({ 'Content-Type': 'application/json' }));
    return this._http.post(`${this._baseUrl}/auth/login`, body, options)
      .map((res: Response) => {
        // login successful if there is a token
        if (res.json().token) {
          // store the token of the user in local storage
          localStorage.setItem('token', res.json().token);
          localStorage.setItem('username', res.json().username);
          localStorage.setItem('member_since', res.json().member_since);
          localStorage.setItem('verified', 'true');
        }
      })
      .catch(this.handleError);
  }

  logout() {
    //remove token from session
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('verified');
    localStorage.removeItem('member_since');
  }

  register(model: any) {
    let body = {
      first_name: model.firstName,
      last_name: model.lastName,
      username: model.username,
      email: model.email,
      password: model.password
    };
    let options = new RequestOptions(new Headers({ 'Content-Type': 'application/json' }));
    return this._http.post(`${this._baseUrl}/auth/register`, body, options)
    .map(this.extractData)
    .catch(this.handleError);

  }

  private extractData(response: Response) {
    let body = response.json();
    return body || {};
  }

  private handleError(error: Response | any) {
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} - ${body['message']} - ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(error.json()['message'])
  }

}
