import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaBecariosComponent } from './lista-becarios.component';

describe('ListaBecariosComponent', () => {
  let component: ListaBecariosComponent;
  let fixture: ComponentFixture<ListaBecariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ListaBecariosComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListaBecariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
