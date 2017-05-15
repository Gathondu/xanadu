import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";

import { DataService } from "../../services/data.service";
import { AlertService } from "../../services/alert.service";

@Component({
  selector: 'items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css'],
})
export class ItemsComponent implements OnInit {

  item = {};
  listId: string;
  constructor(
    private _route: ActivatedRoute,
    private _dataService: DataService,
    private _router: Router,
    private _alert: AlertService
  ) { }

  ngOnInit() {
    this.listId = this._route.snapshot.paramMap.get('bucketlist_id');
    this.getItem()
  }

  getItem() {
    return this._dataService.get('/api/v1.0/bucketlist/' + this.listId + '/items/' + `${this._route.snapshot.paramMap.get('id')}`)
      .subscribe(data => {
        this.item = data;
      });
  }

  editItem(item) {
    let params = [
      { 'list': this.listId },
      { 'id': item.id },
      { 'title': item.title },
      { 'body': item.content }
    ]
    this._router.navigate(['/item-add'], { queryParams: { 'item': JSON.stringify(params) } });
  }

  removeItem(id) {
    this._dataService.delete('/api/v1.0/bucketlist/' + this.listId + '/items/' + id)
      .subscribe(
      data => {
        this._alert.error('Item Deleted', true);
        this._router.navigate(['/bucketlist/' + this.listId])
      },
      error => {
        this._alert.error(error);
      }
      );
  }

  back() {
    this._router.navigate(['/bucketlist/' + this.listId]);
  }
}
