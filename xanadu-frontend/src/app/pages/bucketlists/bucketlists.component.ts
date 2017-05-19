import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";
import { Router } from "@angular/router";

@Component({
  selector: 'bucketlists',
  templateUrl: './bucketlists.component.html',
  styleUrls: ['./bucketlists.component.css'],
})
export class BucketlistsComponent implements OnInit {

  member_since = localStorage.getItem('member_since');
  date = this.member_since.split(',')
  _search = false;
  _paginate = false;
  bucketlist = {};
  constructor(
    private _dataService: DataService,
    private _alert: AlertService,
    private _router: Router
  ) {
  }

  ngOnInit() {
    this.getBucketList();
  }

  getBucketList() {
    // get bucketlist objects
    return this._dataService.get('/api/v1.0/bucketlist/')
      .subscribe(data => {
        this.bucketlist = data;
      },
      error => {
        this._alert.error(error);
      });
  }

  search(title: string) {
    if (title) {
      this._search = true;
    } else {
      this._search = false;
    }
    //search function
    return this._dataService.get('/api/v1.0/bucketlist/?q=' + title)
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
    return this._dataService.get('/api/v1.0/bucketlist/?limit=' + num)
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


  editList(list) {
    let params = [
      { 'id': list.id },
      { 'title': list.title },
      { 'description': list.description }
    ]
    this._router.navigate(['/bucketlist-add'], { queryParams: { 'list': JSON.stringify(params) } });
  }

  removeList(id) {
    this._dataService.delete('/api/v1.0/bucketlist/' + id)
      .subscribe(
      data => {
        this._alert.error('Bucketlist Deleted');
        this.getBucketList();
        window.scrollTo(0, 0);
      },
      error => {
        this._alert.error(error);
      }
      );
  }

}
