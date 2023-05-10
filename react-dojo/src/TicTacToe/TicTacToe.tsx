import { Board } from "./Board";
import { History } from "./History";
import img from "./img.png";
import React, { useState } from 'react';
import { GameInformation } from './GameInformation';


export interface Step {
  player: Player;
  position: number;
}


export enum Player {
  X = 'X',
  O = 'O',
}

const steps: Step[] = [
  {
    player: Player.O,
    position: 0,
  },
  {
    player: Player.X,
    position: 4,
  }
];


export function TicTacToe() {
  const players = useState()

  return (
    <div className="container mx-auto p-4">
      <h1 className="bg-yellow-200 text-black/80 p-2 text-2xl font-bold  rounded">Tic Tac Toe</h1>
      <div className="grid grid-cols-3 gap-4">
        <div className="col-span-2 row-span-1">
          <GameInformation  />
        </div>
        <div className="col-span-2 row-start-2">
          <Board steps={steps} />
        </div>
        <div className="col-span-1 row-span-2">
          <History steps={steps} />
        </div>
      </div>

      <h3>Reference</h3>
      <img src={img} alt="reference image" />
    </div>
  );
}
