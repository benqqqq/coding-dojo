import { Step } from "./Definitions";
import React, { createContext, ReactNode, useContext, useReducer } from "react";
import { getPlayerAtThisPosition, getWinner } from './utils';

const StepsContext = createContext<Step[]>([]);
const StepDispatchContext = createContext<React.Dispatch<Action> | null>(null);

export enum ActionTypes {
  ADD,
  ROLLBACK_TO,
  RESET,
}

interface Action {
  type: ActionTypes;
  payload?: any;
}

export const stepReducer = (state: Step[], action: Action) => {
  switch (action.type) {
    case ActionTypes.ADD:
      const step: Step = action.payload;
      if (getPlayerAtThisPosition(step.position, state) !== null) {
        return state;
      }
      if (getWinner(state) !== null) {
        return state;
      }
      return [...state, action.payload];
    case ActionTypes.ROLLBACK_TO:
      return state.slice(0, action.payload + 1);
    case ActionTypes.RESET:
      return [];
    default:
      return state;
  }
};

export const StepsProvider = ({ children }: { children: ReactNode }) => {
  const [steps, dispatch] = useReducer(stepReducer, []);

  return (
    <StepsContext.Provider value={steps}>
      <StepDispatchContext.Provider value={dispatch}>
        {children}
      </StepDispatchContext.Provider>
    </StepsContext.Provider>
  );
};

export const useSteps = () => {
  return useContext(StepsContext);
};

export const useStepDispatch = () => {
  return useContext(StepDispatchContext) as React.Dispatch<Action>;
};
