import { Component, OnInit } from '@angular/core';

import {BucketlistService} from "../../services/bucketlist.service";
import {AuthenticationService} from "../../services/authentication.service";

@Component({
  selector: 'bucketlists',
  templateUrl: './bucketlists.component.html',
  styleUrls: ['./bucketlists.component.css'],
})
export class BucketlistsComponent implements OnInit {

  errorMessage: string;
  private _baseUrl = 'http://127.0.0.1:5000';
  bucketlist = {};
  token = {};
  constructor(
    private _dataService: BucketlistService,
    private _http: AuthenticationService
  ) { }

  ngOnInit() {
    this.getBucketList();
  }
  getBucketList(){
  }

}
