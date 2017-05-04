import { Injectable } from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from "@angular/router";

@Injectable()
export class AuthguardService implements CanActivate{

  constructor(private _router: Router) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (localStorage.getItem('token')) {
      // logged in
      return true;
    }
    // not logged in so redirect to login page with the return url
    this._router.navigate(['/login'], {queryParams: {returnUrl: state.url}});
    return false;
  }

}
