import { ActionTypes, useStepDispatch, useSteps } from "./StepsContext";

export function History() {
  const steps = useSteps();
  const dispatch = useStepDispatch();
  const handleStepClick = (index: number) => {
    dispatch({
      type: ActionTypes.ROLLBACK_TO,
      payload: index,
    });
  };

  const handleGameStartClick = () => {
    dispatch({
      type: ActionTypes.RESET,
    });
  };

  return (
    <>
      <p className="m-2">Steps :</p>
      <ul>
        <li className="p-1">
          <button
            className="bg-white text-black font-bold"
            onClick={handleGameStartClick}
          >
            Go to Game start
          </button>
        </li>
        {steps.map((step, index) => (
          <li key={index} className="p-1">
            <button
              className="bg-white text-black font-bold"
              onClick={() => handleStepClick(index)}
            >
              Go to move {index + 1}
            </button>
          </li>
        ))}
      </ul>
    </>
  );
}
