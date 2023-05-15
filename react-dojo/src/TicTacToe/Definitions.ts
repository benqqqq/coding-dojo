export enum Player {
  X = 'X',
  O = 'O',
}

export interface Step {
  player: Player;
  position: number;
}