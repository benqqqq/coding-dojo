import "./App.css";
import React from "react";
import { Link } from "react-router-dom";

function App() {
  return (
    <>
      <li>
        <Link to="/tic_tac_toe">Tic Tac Toe</Link>
      </li>
      <li>
        <Link to="/autocomplete">Autocomplete</Link>
      </li>
    </>
  );
}

export default App;
