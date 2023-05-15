import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { TicTacToe } from "./TicTacToe/TicTacToe";
import { AutoComplete } from "./AutoComplete/AutoComplete";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/tic_tac_toe",
    element: <TicTacToe />,
  },
  {
    path: "/autocomplete",
    element: <AutoComplete />,
  },
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
