import { Component, OnInit } from '@angular/core';
import {AlertService} from "../../services/alert.service";

@Component({
  selector: 'alert',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.css']
})
export class AlertComponent implements OnInit {

  message: any;
  constructor(private _alertService: AlertService) { }

  ngOnInit() {
    this._alertService.getMessage().subscribe(message => {this.message = message});
  }

}
