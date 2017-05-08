import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { ActivatedRoute } from "@angular/router";
import { Location } from "@angular/common";

@Component({
  selector: 'list-detail',
  templateUrl: './list-detail.component.html',
  styleUrls: ['./list-detail.component.css']
})
export class ListDetailComponent implements OnInit {

  bucketlist = {};
  item = {};
  constructor(
    private _dataService: DataService,
    private _route: ActivatedRoute,
    private _location: Location
  ) { }

  ngOnInit() {
    this.getList();
  }

  getList() {
    return this._dataService.get('/api/v1.0/bucketlist/' + `${this._route.snapshot.paramMap.get('id')}`+'/items/')
    .subscribe(data => this.bucketlist = data);
  }

  back() {
    this._location.back();
  }
}