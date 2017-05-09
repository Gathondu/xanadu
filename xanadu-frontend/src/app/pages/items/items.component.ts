import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { DataService } from "../../services/data.service";

@Component({
  selector: 'items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css'],
})
export class ItemsComponent implements OnInit {

  item = {};
  constructor(
    private _route: ActivatedRoute,
    private _dataService: DataService,
    private _router: Router
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
    this._router.navigate(['/bucketlist'])
  }
}
