import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";

import { DataService } from "../app/services/data.service";
import { fadeInAnimation } from "../app/pages/animations/index";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],

  // make animations available
  animations: [fadeInAnimation],

  // attach the animation to the host (root) element of this component
  host: {'[@fadeInAnimation]': ''}
})
export class AppComponent implements OnInit {
  verified: boolean;
  username = localStorage.getItem('username');
  constructor(private _router: Router) { }
  ngOnInit() {
  }
}
