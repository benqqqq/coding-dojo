/*jshint esversion: 6 */

const combine = (str) => {
  if (typeof str === "undefined") {
    return "";
  }
  // a function that return str
  return (nestedStr) => {
    if (typeof nestedStr === "undefined") {
      return str;
    }
    return combine(`${str}-${nestedStr}`);
  };
};

console.log(combine()); // ''
console.log(combine("a")()); // a
console.log(combine("a")("b")()); // a-b
console.log(combine("a")("b")("c")()); // a-b-c
