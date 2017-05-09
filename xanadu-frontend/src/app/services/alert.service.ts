import { Injectable } from '@angular/core';
import {Subject} from "rxjs/Subject";
import {NavigationStart, Router} from "@angular/router";
import {Observable} from "rxjs";

@Injectable()
export class AlertService {
  private subject = new Subject<any>();
  private keepAfterNavigationChange = false;

  constructor(private _router: Router) {
    // clear alert message on route change
    _router.events.subscribe(event => {
        if (event instanceof NavigationStart) {
          if (this.keepAfterNavigationChange) {
            // keep once for single navigation
            this.keepAfterNavigationChange = false;
          }else {
            // clear the alert
            this.subject.next();
          }
        }
      }
    );
  }

  success(message: string, keepAfterNavigationChange = false) {
    this.keepAfterNavigationChange = keepAfterNavigationChange;
    this.subject.next({type: 'success', text: message});
  }

  error(message: string, keepAfterNavigationChange = false) {
    this.keepAfterNavigationChange = keepAfterNavigationChange;
    this.subject.next({type: 'error', text: message});
  }

  getMessage(): Observable<any> {
    return this.subject.asObservable();
  }
}
