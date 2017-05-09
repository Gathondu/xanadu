import { Component, OnInit } from '@angular/core';
import { DataService } from "../app/services/data.service";
import { Router } from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  verified: boolean;
  username = localStorage.getItem('username');
  constructor(private _router: Router) { }
  ngOnInit() {
  }
}
