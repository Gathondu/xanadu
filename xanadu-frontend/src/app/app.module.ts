import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import {RouterModule, Routes} from "@angular/router";

import { AppComponent } from './app.component';
import { BucketlistsComponent } from './pages/bucketlists/bucketlists.component';
import { LoginComponent } from './pages/login/login.component';
import { AlertComponent } from './pages/alert/alert.component';
import {BucketlistService} from "./services/bucketlist.service";
import {AuthenticationService} from "./services/authentication.service";

const routes: Routes = [
  {path: '', redirectTo:'/login', pathMatch: 'full'},
  {path: 'login', component: LoginComponent},
  {path: 'bucketlist', component: BucketlistsComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    BucketlistsComponent,
    LoginComponent,
    AlertComponent
  ],
  imports: [
    RouterModule.forRoot(routes),
    BrowserModule,
    FormsModule,
    HttpModule,
    JsonpModule
  ],
  providers: [
    BucketlistService,
    AuthenticationService
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
