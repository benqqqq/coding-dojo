import { Shape } from "./Shape";
import { getNextPlayer, getPlayerAtThisPosition } from "./utils";
import { ActionTypes, useStepDispatch, useSteps } from "./StepsContext";

export function Board() {
  const steps = useSteps();
  const dispatch = useStepDispatch();

  const handleClickCell = (position: number) => {
    dispatch({
      type: ActionTypes.ADD,
      payload: {
        player: getNextPlayer(steps),
        position: position,
      },
    });
  };

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
                onClick={() => handleClickCell(index)}
              >
                {getPlayerAtThisPosition(index, steps) === "X" && (
                  <Shape square />
                )}
                {getPlayerAtThisPosition(index, steps) === "O" && (
                  <Shape circle />
                )}
                {getPlayerAtThisPosition(index, steps) === null && (
                  <div className="invisible group-hover:visible w-full h-full opacity-30">
                    {getNextPlayer(steps) === "X" && <Shape square />}
                    {getNextPlayer(steps) === "O" && <Shape circle />}
                  </div>
                )}
              </div>
            ))}
        </div>
      </div>
    </>
  );
}
