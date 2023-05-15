import { Step } from "./Definitions";
import { useSteps } from "./StepsContext";
import { getNextPlayer, getWinner } from "./utils";

export function GameInformation() {
  const steps = useSteps();

  return (
    <div className="px-5 py-3">
      <p>Next Plater : {getNextPlayer(steps)}</p>
      <p>Winner : {getWinner(steps)}</p>
    </div>
  );
}
