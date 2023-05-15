import { Shape } from "./Shape";
import { Meta, StoryObj } from "@storybook/react";

const meta = {
  title: "TicTacToe/Shape",
  component: Shape,
  tags: [],
  argTypes: {},
} satisfies Meta<typeof Shape>;

export default meta;

type Story = StoryObj<typeof meta>;

export const Square: Story = {
  render: () => (
    <div className="h-20 w-20">
      <Shape square />
    </div>
  ),
};

export const Circle: Story = {
  render: () => (
    <div className="h-20 w-20">
      <Shape circle />
    </div>
  ),
}
