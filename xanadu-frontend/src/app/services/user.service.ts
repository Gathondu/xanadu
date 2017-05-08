import { Injectable } from '@angular/core';
import { AuthenticationService } from "app/services/authentication.service";
import { RequestOptions, Http, Response, Headers } from "@angular/http";
import { Observable } from "rxjs/Rx";

@Injectable()
export class UserService {

  private _baseUrl = 'http://127.0.0.1:5000';
  constructor(
    private _http: Http
  ) { }

  login(username: string, password: string){
    let body = JSON.stringify({username: username, password: password});
    let options = new RequestOptions(new Headers({'Content-Type': 'application/json'}));
    return this._http.post(`${this._baseUrl}/auth/login`, body, options)
      .map((res: Response) => {
      // login successful if there is a token
        if (res.json().token) {
          // store the token of the user in local storage
          localStorage.setItem('token', res.json().token);
          localStorage.setItem('username', res.json().username);
    }
      })
      .catch(this.handleError);
  }

  logout() {
    //remove token from session
    localStorage.removeItem('token');
    localStorage.removeItem('username');
  }

  private extractData(response: Response) {
    let body = response.json();
    return body || {};
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
