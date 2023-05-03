import { Board } from "./Board";
import { History } from "./History";
import img from "./img.png";
import React, { useState } from 'react';
import { GameInformation } from './GameInformation';

export function TicTacToe() {
  const players = useState()

  return (
    <>
      <h1>Tic Tac Toe</h1>
      <div></div>
      <GameInformation />
      <Board />
      <History />

      <h3>Reference</h3>
      <img src={img} alt="reference image" />
    </>
  );
}
