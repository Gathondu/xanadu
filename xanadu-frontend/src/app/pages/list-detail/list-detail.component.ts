import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { ActivatedRoute, Router } from "@angular/router";

import { AlertService } from "../../services/alert.service";

@Component({
  selector: 'list-detail',
  templateUrl: './list-detail.component.html',
  styleUrls: ['./list-detail.component.css']
})
export class ListDetailComponent implements OnInit {

  _search = false;
  _paginate = false;
  bucketlist = {};
  item = {};
  constructor(
    private _dataService: DataService,
    private _route: ActivatedRoute,
    private _router: Router,
    private _alert: AlertService
  ) { }

  ngOnInit() {
    this.getList();
  }

  getList() {
    return this._dataService.get('/api/v1.0/bucketlist/' + `${this._route.snapshot.paramMap.get('id')}` + '/items/')
      .subscribe(data => this.bucketlist = data);
  }

  addItem() {
    this._router.navigate(['/item-add'], { queryParams: { 'id': this.bucketlist['bucketlist_id'] } });
  }

  editItem(item) {
    let params = [
      { 'list': this.bucketlist['bucketlist_id'] },
      { 'id': item.id },
      { 'title': item.title },
      { 'body': item.content }
    ]
    this._router.navigate(['/item-add'], { queryParams: { 'item': JSON.stringify(params) } });
  }
  search(title: string) {
    if (title) {
      this._search = true;
    } else {
      this._search = false;
    }
    //search function
    return this._dataService.get('/api/v1.0/bucketlist/' + `${this._route.snapshot.paramMap.get('id')}` + '/items/?q=' + title)
      .subscribe(data => {
        this.bucketlist = data;
      },
      error => {
        this._alert.error(error);
      });
  }
    paginate(num: number) {
    if (num) {
      this._paginate = true;
    } else {
      this._paginate = false;
    }
    //search function
    return this._dataService.get('/api/v1.0/bucketlist/' + `${this._route.snapshot.paramMap.get('id')}` + '/items/?limit=' + num)
      .subscribe(data => {
        this.bucketlist = data;
      },
      error => {
        this._alert.error(error);
      });
  }

  goTo(url: string) {
    if(url) {
    return this._dataService.get(url)
      .subscribe(data =>
      { this.bucketlist = data; },
      error => { this._alert.error(error); }
      );
    }
  }

  removeItem(id) {
    this._dataService.delete('/api/v1.0/bucketlist/' + this.bucketlist['bucketlist_id'] + '/items/' + id)
      .subscribe(
      data => {
        this._alert.error('Item Deleted');
        this.getList();
        window.scrollTo(0, 0);
      },
      error => {
        this._alert.error(error);
      }
      );
  }

  back() {
    this._router.navigate(['/bucketlist'])
  }
}
