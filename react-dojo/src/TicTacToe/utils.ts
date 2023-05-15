import { Player, Step } from "./Definitions";

export const getNextPlayer = (steps: Step[]): Player => {
  return steps.length % 2 === 0 ? Player.O : Player.X;
};
export const getPlayerAtThisPosition = (
  position: number,
  steps: Step[]
): Player | null => {
  return steps.find((step) => step.position === position)?.player ?? null;
};

export const resetSteps = (): Step[] => {
  return [];
};
export const rollbackToStep = (index: number, steps: Step[]): Step[] => {
  return steps.slice(0, index);
};

export const getWinner = (steps: Step[]): Player | null => {
  const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (const combination of winningCombinations) {
    const [a, b, c] = combination;
    const playerAtA = getPlayerAtThisPosition(a, steps);
    const playerAtB = getPlayerAtThisPosition(b, steps);
    const playerAtC = getPlayerAtThisPosition(c, steps);
    if (playerAtA && playerAtB && playerAtC && playerAtA === playerAtB && playerAtA === playerAtC) {
      return playerAtA;
    }
  }
  return null;
};
