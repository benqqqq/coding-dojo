import { Step } from "./TicTacToe";

export function History({ steps }: { steps: Step[] }) {
  return (
    <>
      <p className="m-2">Steps :</p>
      <ul>
        <li className="p-1">
          <button className="bg-white text-black font-bold">Go to Game start</button>
        </li>
        {steps.map((step, index) => (
          <li key={index} className="p-1">
            <button className="bg-white text-black font-bold">Go to move {index}</button>
          </li>
        ))}
      </ul>
    </>
  );
}
