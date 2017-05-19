import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { AlertService } from "../../services/alert.service";
import { UserService } from "../../services/user.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  model: any = {};
  loading = false;
  constructor(
    private _router: Router,
    private _user: UserService,
    private _alert: AlertService
  ) { }

  ngOnInit() {
  }
  register() {
    this.loading = true;
    this._user.register(this.model)
      .subscribe(
      data => {
        // set success message and pass true paramater to persist the message after redirecting to the login page
        this._alert.success('Registration successful', true);
        this._router.navigate(['/login']);
      },
      error => {
        this._alert.error(error);
        this.loading = false
      }
      );
  }

}
