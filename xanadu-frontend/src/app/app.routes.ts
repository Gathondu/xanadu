import { Routes } from "@angular/router";
import { LoginComponent } from "app/pages/login/login.component";
import { AuthguardService } from "app/services/authguard.service";
import { BucketlistsComponent } from "app/pages/bucketlists/bucketlists.component";
import { AppComponent } from "app/app.component";
import { ListDetailComponent } from "app/pages/list-detail/list-detail.component";
import { ItemsComponent } from "app/pages/items/items.component";
import { RegisterComponent } from "app/pages/register/register.component";

export const AppRoutes = [
  { path: 'login', component: LoginComponent },
  {
    path: '',
    redirectTo: '/bucketlist',
    pathMatch: 'full'
  },
  {
    path: 'bucketlist',
    canActivate: [AuthguardService],
    component: BucketlistsComponent
  },
  {
    path: 'bucketlist/:id',
    canActivate: [AuthguardService],
    component: ListDetailComponent
  },
  {
    path: 'items/:location',
    canActivate: [AuthguardService],
    component: ItemsComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  }
];
