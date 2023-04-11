export default class TennisGame {
  private _playerTwoScore = 0;
  private _playerOneScore = 0;

  private map = new Map<number, string>();

  constructor(private playerOneName: string, private playerTwoName: string) {
    this.map.set(0, 'Love');
    this.map.set(1, 'Fifteen');
    this.map.set(2, 'Thirty');
    this.map.set(3, 'Forty');
  }

  score() {
    if (this.isTie()) {
      if (this.isDeuce()) {
        return 'Deuce';
      } else {
        return `${this.playerOneScoreName} All`;
      }
    } else {
      if (this._playerOneScore === 5) {
        return `${this.playerOneName} Win`;
      }
      if (this._playerTwoScore === 5) {
        return `${this.playerTwoName} Win`;
      }
      if (this._playerOneScore === 4) {
        return `${this.playerOneName} Adv`;
      }
      if (this._playerTwoScore === 4) {
        return `${this.playerTwoName} Adv`;
      }

      return `${this.playerOneScoreName} ${this.playerTwoScoreName}`;
    }
  }

  private isDeuce() {
    return this._playerOneScore >= 3;
  }

  private isTie() {
    return this._playerOneScore === this._playerTwoScore;
  }

  get playerOneScoreName() {
    return this.map.get(this._playerOneScore);
  }

  get playerTwoScoreName() {
    return this.map.get(this._playerTwoScore);
  }

  playerOneScore() {
    this._playerOneScore += 1;
  }

  playerTwoScore() {
    this._playerTwoScore += 1;
  }
}
