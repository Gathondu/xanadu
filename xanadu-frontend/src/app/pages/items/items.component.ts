import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { DataService } from "../../services/data.service";
import { Location } from "@angular/common";

@Component({
  selector: 'items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit {

  item = {};
  constructor(
    private _route: ActivatedRoute,
    private _dataService: DataService,
    private _location: Location
  ) { }

  ngOnInit() {
    this.getItem()
  }

  getItem() {
    return this._dataService.get(`${this._route.snapshot.paramMap.get('location')}`)
      .subscribe(data => {
        this.item = data;
      });
  }
  back() {
    this._location.back();
  }
}
