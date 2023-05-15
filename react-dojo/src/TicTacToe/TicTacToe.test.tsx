import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { TicTacToe } from "./TicTacToe";

describe("TicTacToe", () => {
  it("should render", () => {
    render(<TicTacToe />);
    expect(screen.getByText(/Tic Tac Toe/i)).toBeTruthy()

  });
});
