import { Component } from '@angular/core';
import { DataService } from "../app/services/data.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = `Welcome to your Bucketlist ${localStorage.getItem('username')}`;
  errorMessage: string;
  bucketlist = {};
  constructor(
    private _dataService: DataService
  ) { }

  ngOnInit() {
    this.getBucketList();
  }

  getBucketList() {
    // get bucketlist objects
    return this._dataService.get('/api/v1.0/bucketlist/')
      .subscribe(data => {
        this.bucketlist = data;
      });
  }
}
