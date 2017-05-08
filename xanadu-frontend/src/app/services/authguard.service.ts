import { Injectable } from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from "@angular/router";
import { Http, RequestOptions, Response, Headers} from "@angular/http";
import { Observable } from "rxjs/Rx";

@Injectable()
export class AuthguardService implements CanActivate {

  private _baseUrl = 'http://127.0.0.1:5000';
  constructor(
    private _router: Router,
    private _http: Http
    ) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    this.verifyToken()
    .subscribe(data => {
      localStorage.setItem('verified', data);
    });
    if (localStorage.getItem('verified') == 'true') {
      // logged in
      return true;
    }
    // not logged in so redirect to login page with the return url
    this._router.navigate(['/login'], {queryParams: {returnUrl: state.url}});
    return false;
  }
  verifyToken() {
    let token: any;
    let url = `${this._baseUrl}/auth/verify`;
    let body = JSON.stringify({'token': localStorage.getItem('token')});
    let headers = new Headers({'Content-Type': 'application/json'});
    let options = new RequestOptions({headers: headers})
    return this._http.post(url, body, options)
    .map(this.extractData)
    .catch(this.handleError);
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
