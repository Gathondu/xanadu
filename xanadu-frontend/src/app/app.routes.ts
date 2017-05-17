import { Routes } from "@angular/router";
import { LoginComponent } from "app/pages/login/login.component";
import { AuthguardService } from "app/services/authguard.service";
import { BucketlistsComponent } from "app/pages/bucketlists/bucketlists.component";
import { AppComponent } from "app/app.component";
import { ListDetailComponent } from "app/pages/list-detail/list-detail.component";
import { ItemsComponent } from "app/pages/items/items.component";
import { RegisterComponent } from "app/pages/register/register.component";
import { BucketlistFormComponent } from "app/pages/bucketlist-form/bucketlist-form.component";
import { ItemFormComponent } from "app/pages/item-form/item-form.component";
import { HomeComponent } from "app/pages/home/home.component";

export const AppRoutes = [
  { path: 'login', component: LoginComponent },
  { path: 'index', component: HomeComponent },
  {
    path: '',
    redirectTo: '/index',
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
    path: 'bucketlist-add',
    canActivate: [AuthguardService],
    component: BucketlistFormComponent
  },
  {
    path: 'item-add',
    canActivate: [AuthguardService],
    component: ItemFormComponent
  },
  {
    path: 'bucketlist/:bucketlist_id/items/:id',
    canActivate: [AuthguardService],
    component: ItemsComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: '**',
    redirectTo: '/index',
    pathMatch: 'full'
  }
];
