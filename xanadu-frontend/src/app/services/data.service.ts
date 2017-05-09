import { Injectable } from '@angular/core';
import { RequestOptions, Http, Response, Headers } from "@angular/http";
import { Observable } from "rxjs/Rx";


@Injectable()
export class DataService {

  private _baseUrl = 'http://127.0.0.1:5000';
  constructor(
    private _http: Http,
  ) { }

  createHeader(): Headers{
    let headers = new Headers();
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Authorization', 'Token ' + localStorage.getItem('token') );
    headers.append('Content-Type', 'application/json');
    return headers
  }

  get(url) {
    url = `${this._baseUrl + url}`;
    let headers = this.createHeader();
    let options = new RequestOptions({ headers });
    return this._http.get(url, options)
      .map(this.extractData)
      .catch(this.handleError);
  }

  post(url, body) {
    url = `${this._baseUrl + url}`;
    let headers = this.createHeader();
    let options = new RequestOptions({headers});
    body = JSON.stringify(body);
    return this._http.post(url, body, options)
    .map(this.extractData)
    .catch(this.handleError);
  }

  put(url, body) {
    url = `${this._baseUrl + url}`;
    console.log(url);
    let headers = this.createHeader();
    let options = new RequestOptions({headers});
    body = JSON.stringify(body);
    return this._http.put(url, body, options)
    .map(this.extractData)
    .catch(this.handleError);
  }

  delete(url) {
    url = `${this._baseUrl + url}`;
    let headers = this.createHeader();
    let options = new RequestOptions({ headers });
    return this._http.delete(url, options)
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
      errMsg = `${error.status} - ${error.statusText || ''} - ${body['message']} ${err}`;
    }else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(error.json()['message'])
  }

}
