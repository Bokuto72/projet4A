import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-choose-ai-difficulty-vs-player',
  templateUrl: './choose-ai-difficulty-vs-player.page.html',
  styleUrls: ['./choose-ai-difficulty-vs-player.page.scss'],
})
export class ChooseAiDifficultyVsPlayerPage implements OnInit {

  constructor(private router: Router) {}

  ngOnInit() {}
  goHome() {
    this.router.navigate(['/tabs/tab1']);
  }
  goToPlayerVsAIPage(difficulty: string) {
    this.router.navigate(['/player-vs-ai', {difficulty}]); // Remplace '/player-vs-ai' par le chemin de ta page "player-vs-ai"
  }
}