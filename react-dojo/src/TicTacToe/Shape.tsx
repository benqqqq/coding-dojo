import React from "react";

const Square = () => {
  return (
    <div className="w-full h-full relative">
      <div className="absolute top-0 left-1/2 w-1 bg-black rotate-45 h-full"></div>
      <div className="absolute top-0 left-1/2 w-1 bg-black -rotate-45 h-full"></div>
    </div>
  );
};

function Circle() {
  return (
    <div className="w-full h-full relative">
      <div className="absolute top-1/2 left-1/2 rounded-full border-4 border-black w-4/5 h-4/5 -translate-x-1/2 -translate-y-1/2"></div>
    </div>
  );
}

interface ShapeProps {
  circle?: boolean;
  square?: boolean;
}

export const Shape = ({ circle, square } : ShapeProps) => {
  return circle ? <Circle /> : square ? <Square /> : <div />;
}