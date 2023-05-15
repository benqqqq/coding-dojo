import { describe, expect, it } from "vitest";
import { ActionTypes, stepReducer } from "./StepsContext";
import { Player } from "./Definitions";

describe("stepReducer", () => {
  it("should return new step after ADD", () => {
    expect(
      stepReducer([], {
        type: ActionTypes.ADD,
        payload: { position: 1, player: Player.O },
      })
    ).toEqual([{ position: 1, player: Player.O }]);

    expect(
      stepReducer(
        [
          {
            position: 1,
            player: Player.O,
          },
        ],
        {
          type: ActionTypes.ADD,
          payload: { position: 3, player: Player.X },
        }
      )
    ).toEqual([
      { position: 1, player: Player.O },
      { position: 3, player: Player.X },
    ]);
  });

  it("should not return new step after ADD if position exist", () => {
    expect(
      stepReducer(
        [
          {
            position: 1,
            player: Player.O,
          },
        ],
        {
          type: ActionTypes.ADD,
          payload: { position: 1, player: Player.X },
        }
      )
    ).toEqual([{ position: 1, player: Player.O }]);
  });
  it("should not return new step after winner exist", () => {
    expect(
      stepReducer(
        [
          {
            position: 0,
            player: Player.O,
          },
          {
            position: 1,
            player: Player.O,
          },
          {
            position: 2,
            player: Player.O,
          },
        ],
        {
          type: ActionTypes.ADD,
          payload: { position: 3, player: Player.X },
        }
      )
    ).toEqual([
      {
        position: 0,
        player: Player.O,
      },
      {
        position: 1,
        player: Player.O,
      },
      {
        position: 2,
        player: Player.O,
      },
    ]);
  });

  it("should return history step after ROLLBACK_TO", () => {
    expect(
      stepReducer(
        [
          {
            position: 3,
            player: Player.O,
          },
          {
            position: 5,
            player: Player.X,
          },
        ],
        {
          type: ActionTypes.ROLLBACK_TO,
          payload: 0,
        }
      )
    ).toEqual([
      {
        position: 3,
        player: Player.O,
      },
    ]);
  });
  it("should return empty steps after RESET", () => {
    expect(
      stepReducer(
        [
          {
            position: 3,
            player: Player.O,
          },
        ],
        {
          type: ActionTypes.RESET,
        }
      )
    ).toEqual([]);
  });
});
