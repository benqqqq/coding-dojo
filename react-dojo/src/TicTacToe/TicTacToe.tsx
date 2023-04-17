import { Board } from "./Board";
import { Control } from "./Control";
import img from "./img.png";
import { useState } from 'react';

export function TicTacToe() {
  const players = useState()

  return (
    <>
      <h1>Tic Tac Toe</h1>
      <Board />
      <Control />

      <h3>Reference</h3>
      <img src={img} alt="reference image" />
    </>
  );
}
