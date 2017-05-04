import { Injectable } from '@angular/core';
import {Http, Response} from "@angular/http";

import 'rxjs/add/operator/map';
import {AuthenticationService} from "./authentication.service";

@Injectable()
export class BucketlistService {
  private _baseUrl = 'http://127.0.0.1:5000';

  bucketlist = {}
  errorMessage: string;

  constructor(
    private _http: AuthenticationService
  ) { }

  getBucketList() {
    //get bucketlist objects
    // this._http.get(`${this._baseUrl}/api/v1.0/bucketlists`)
    //   .subscribe(
    //     bucketlist => this.bucketlist = bucketlist || {},
    //     error => this.errorMessage = <any>error
    //   );
    // return this.bucketlist
  }
}
