import { Meta, StoryObj } from "@storybook/react";
import React from "react";
import { Board } from "./Board";

const meta = {
  title: "TicTacToe/Board",
  component: Board,
  tags: [],
  argTypes: {},
} satisfies Meta<typeof Board>;

export default meta;

type Story = StoryObj<typeof meta>;

export const BoardDemo: Story = {
};
