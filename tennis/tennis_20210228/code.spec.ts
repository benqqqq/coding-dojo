import TennisGame from './code';

function playerOneScore(game: TennisGame, count: number) {
  for (let i = 0; i < count; ++i) {
    game.playerOneScore();
  }
}

function playerTwoScore(game: TennisGame, count: number) {
  for (let i = 0; i < count; ++i) {
    game.playerTwoScore();
  }
}

describe('Tennis Game', () => {
  it('should be Love All', () => {
    const game = new TennisGame('Liz', 'Dz');

    expect(game.score()).toBe('Love All');
  });

  it('should be Fifteen All', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 1);
    playerTwoScore(game, 1);
    expect(game.score()).toBe('Fifteen All');
  });

  it('should be Love Fifteen', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerTwoScore(game, 1);
    expect(game.score()).toBe('Love Fifteen');
  });

  it('should be Love Thirty', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerTwoScore(game, 2);
    expect(game.score()).toBe('Love Thirty');
  });

  it('should be Fifteen Love', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 1);
    expect(game.score()).toBe('Fifteen Love');
  });

  it('should be Thirty Love', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 2);
    expect(game.score()).toBe('Thirty Love');
  });

  it('should be Forty Love', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 3);
    expect(game.score()).toBe('Forty Love');
  });

  it('should be Deuce', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 3);
    playerTwoScore(game, 3);
    expect(game.score()).toBe('Deuce');
  });

  it('should be Adv Deuce', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 4);
    playerTwoScore(game, 4);
    expect(game.score()).toBe('Deuce');
  });

  it('should be Liz Win', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 5);
    expect(game.score()).toBe('Liz Win');
  });

  it('should be Dz Win', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerTwoScore(game, 5);
    expect(game.score()).toBe('Dz Win');
  });

  it('should be Liz Adv', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerOneScore(game, 4);
    expect(game.score()).toBe('Liz Adv');
  });

  it('should be Dz Adv', () => {
    const game = new TennisGame('Liz', 'Dz');
    playerTwoScore(game, 4);
    expect(game.score()).toBe('Dz Adv');
  });
});
