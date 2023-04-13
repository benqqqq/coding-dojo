import { useState } from "react";
import "./App.css";
import { products, user } from "./data";

function MyButton() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <>
      <button onClick={handleClick}>Click me!</button>
      {count > 0 && <p>You clicked {count} times</p>}
    </>
  );
}

function AboutPage() {
  return (
    <>
      <h1>About</h1>
      <p>This is the about page</p>
    </>
  );
}

function App() {
  return (
    <div className="App">
      <h1>Welcome to my app</h1>
      <MyButton />
      <MyButton />
      <AboutPage />
      <h1>{user.name}</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>{product.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
