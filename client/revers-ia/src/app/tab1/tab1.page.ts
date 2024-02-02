import { Component } from '@angular/core';
import { NavController } from '@ionic/angular';
import { Router } from '@angular/router';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})

export class Tab1Page {

  constructor(private router: Router) {}

  goToOfflinePage() {
    this.router.navigate(['/offline']); // Remplace '/offline' par le chemin de ta page "offline"
  }

}
