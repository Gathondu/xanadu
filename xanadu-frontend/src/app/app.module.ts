import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import {RouterModule, Routes} from "@angular/router";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { BucketlistsComponent } from './pages/bucketlists/bucketlists.component';
import { LoginComponent } from './pages/login/login.component';
import { AlertComponent } from './pages/alert/alert.component';
import {AuthenticationService} from "./services/authentication.service";
import {AuthguardService} from "./services/authguard.service";
import { RegisterComponent } from './pages/register/register.component';
import { DataService } from "app/services/data.service";
import { AppRoutes } from "app/app.routes";
import { ListDetailComponent } from './pages/list-detail/list-detail.component';
import { AlertService } from "app/services/alert.service";
import { ItemsComponent } from './pages/items/items.component';
import { UserService } from "app/services/user.service";
import { BucketlistFormComponent } from './pages/bucketlist-form/bucketlist-form.component';
import { ItemFormComponent } from './pages/item-form/item-form.component';


@NgModule({
  declarations: [
    AppComponent,
    BucketlistsComponent,
    LoginComponent,
    AlertComponent,
    RegisterComponent,
    ListDetailComponent,
    ItemsComponent,
    BucketlistFormComponent,
    ItemFormComponent,
  ],
  imports: [
    RouterModule.forRoot(AppRoutes),
    BrowserModule,
    FormsModule,
    HttpModule,
    BrowserAnimationsModule
  ],
  providers: [
    AuthenticationService,
    AuthguardService,
    DataService,
    AlertService,
    UserService
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
