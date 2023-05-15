import { Board } from "./Board";
import { History } from "./History";
import img from "./img.png";
import React, { useState } from "react";
import { GameInformation } from "./GameInformation";
import { getNextPlayer, getPlayerAtThisPosition } from "./utils";
import { Step } from "./Definitions";
import { StepsProvider } from "./StepsContext";

export function TicTacToe() {
  return (
    <StepsProvider>
      <div className="container mx-auto p-4">
        <h1 className="bg-yellow-200 text-black/80 p-2 text-2xl font-bold  rounded">
          Tic Tac Toe
        </h1>
        <div className="grid grid-cols-3 gap-4">
          <div className="col-span-2 row-span-1">
            <GameInformation />
          </div>
          <div className="col-span-2 row-start-2">
            <Board />
          </div>
          <div className="col-span-1 row-span-2">
            <History />
          </div>
        </div>

        <h3>Reference</h3>
        <img src={img} alt="reference image" />
      </div>
    </StepsProvider>
  );
}
