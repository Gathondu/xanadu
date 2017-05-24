import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { MdDialog, MdDialogRef } from "@angular/material";
import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";
import { BucketlistFormComponent } from "../../pages/bucketlist-form/bucketlist-form.component";

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
  list = {};
  constructor(
    private _dataService: DataService,
    private _alert: AlertService,
    private _router: Router,
    public dialog: MdDialog
  ) { }

  ngOnInit() {
    this.getBucketList();
  }

  getBucketList() {
    // get bucketlist objects
    return this._dataService.get('/api/v1.0/bucketlist/')
      .subscribe(data => {
        this.bucketlist = data;
        if (this.bucketlist['count'] == 0) {
          this._alert.warning("You currently don't have any lists.")
        }
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
        if (this.bucketlist['count'] == 0) {
          this._alert.warning("You're search did not match any bucketlist")
        }
      },
      error => {
        this._alert.error(error);
      });
  }

  paginate(num: number) {
    if (num > 0) {
      this._paginate = true;
    } else {
      this._paginate = false;
    }
    return this._dataService.get('/api/v1.0/bucketlist/?limit=' + num)
      .subscribe(data => {
        if (num == 0) {
          this._alert.error("The least items on the list must be one or greater");
        }else{
          this.bucketlist = data;
        }
      },
      error => {
        this._alert.error(error);
      });
  }

  goTo(url: string) {
    if (url) {
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

  openDialog() {
    let dialogRef = this.dialog.open(BucketlistFormComponent, {
      height: '400px',
      width: '600px',
    });
  }
}
