import { Player, Step } from "./TicTacToe";
import { Fragment } from "react";

function Square() {
  return (
    <div className="w-full h-full relative">
      <div className="absolute top-0 left-1/2 w-1 bg-black rotate-45 h-full"></div>
      <div className="absolute top-0 left-1/2 w-1 bg-black -rotate-45 h-full"></div>
    </div>
  );
}

function Circle() {
  return (
    <div className="w-full h-full relative">
      <div className="absolute top-1/2 left-1/2 rounded-full border-4 border-black w-4/5 h-4/5 -translate-x-1/2 -translate-y-1/2"></div>
    </div>
  );
}

const getPlayerAtThisPosition = (
  position: number,
  steps: Step[]
): Player | null => {
  return steps.find((step) => step.position === position)?.player ?? null;
};

const getNextPlayer = (steps: Step[]): Player => {
  return steps.length % 2 === 0 ? Player.O : Player.X;
};

export function Board({ steps }: { steps: Step[] }) {
  return (
    <>
      <div className="flex flex-col items-center justify-center">
        <div className="grid grid-cols-3">
          {Array(9)
            .fill(0)
            .map((_, index) => (
              <div
                key={index}
                className={`
                  h-24 w-24 border-2 border-black bg-yellow-200 rounded group ${
                    getPlayerAtThisPosition(index, steps) === null &&
                    "cursor-pointer hover:bg-yellow-300"
                  }`}
              >
                {getPlayerAtThisPosition(index, steps) === "X" && <Square />}
                {getPlayerAtThisPosition(index, steps) === "O" && <Circle />}
                {
                  getPlayerAtThisPosition(index, steps) === null && (
                    <div className="invisible group-hover:visible w-full h-full opacity-30">
                      {getNextPlayer(steps) === "X" && <Square />}
                      {getNextPlayer(steps) === "O" && <Circle />}
                    </div>
                  )
                }
              </div>
            ))}
        </div>
      </div>
    </>
  );
}
