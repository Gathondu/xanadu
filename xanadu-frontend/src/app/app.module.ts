import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import {RouterModule, Routes} from "@angular/router";

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


@NgModule({
  declarations: [
    AppComponent,
    BucketlistsComponent,
    LoginComponent,
    AlertComponent,
    RegisterComponent,
    ListDetailComponent,
    ItemsComponent,
  ],
  imports: [
    RouterModule.forRoot(AppRoutes),
    BrowserModule,
    FormsModule,
    HttpModule,
    JsonpModule
  ],
  providers: [
    AuthenticationService,
    AuthguardService,
    DataService,
    AlertService
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
