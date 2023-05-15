import { describe, expect, it } from "vitest";
import { getNextPlayer, getPlayerAtThisPosition, getWinner, rollbackToStep } from "./utils";
import { Player } from "./Definitions";

describe("getNextPlayer", () => {
  it("should return the next player", () => {
    expect(getNextPlayer([])).toBe(Player.O);
    expect(getNextPlayer([{ position: 1, player: Player.O }])).toBe(Player.X);
    expect(
      getNextPlayer([
        { position: 1, player: Player.O },
        { position: 5, player: Player.X },
      ])
    ).toBe(Player.O);
  });
});

describe("getPlayerAtThisPosition", () => {
  it("should return the player at this position", () => {
    expect(getPlayerAtThisPosition(1, [])).toBe(null);
    expect(
      getPlayerAtThisPosition(1, [{ position: 1, player: Player.O }])
    ).toBe(Player.O);
    expect(
      getPlayerAtThisPosition(5, [
        { position: 1, player: Player.O },
        { position: 5, player: Player.X },
        { position: 7, player: Player.O },
      ])
    ).toBe(Player.X);
  });
});

describe("getWinner", () => {
  it("should return the winner", () => {
    expect(
      getWinner([
        { position: 1, player: Player.O },
        { position: 5, player: Player.X },
        { position: 7, player: Player.O },
      ])
    ).toBe(null);

    expect(
      getWinner([
        { position: 0, player: Player.O },
        { position: 1, player: Player.O },
        { position: 2, player: Player.O },
      ])
    ).toBe(Player.O);
  });
})