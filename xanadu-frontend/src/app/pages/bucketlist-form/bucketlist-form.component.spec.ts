import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BucketlistFormComponent } from './bucketlist-form.component';

describe('BucketlistFormComponent', () => {
  let component: BucketlistFormComponent;
  let fixture: ComponentFixture<BucketlistFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BucketlistFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BucketlistFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
