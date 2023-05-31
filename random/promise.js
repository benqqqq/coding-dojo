/*jshint esversion: 6 */

class MyPromise {
  constructor(func) {
    this.thenableFuncs = [];

    const resolve = (val) => {
      let result = val;
      this.thenableFuncs.forEach((f) => {
        result = f(result);
      });
    };

    func(resolve);
  }

  then(thenableFunc) {
    this.thenableFuncs.push(thenableFunc);
    return new MyPromise((resolve) => {
      this.thenableFuncs.push((val) => {
        resolve(val);
      });
    });
  }
}

const fetchUserDetails = () => {
  return new MyPromise((resolve, reject) => {
    // Simulating an API call
    console.log("start to fetch user");
    setTimeout(() => {
      const userDetails = {
        name: "Jane Doe",
        age: 25,
        email: "jane@example.com",
      };
      resolve(userDetails);
    }, 1000);
  });
};

fetchUserDetails()
  .then((value) => {
    console.log("Promise resolved with value:", value);
    return "nextValue";
  })
  .then((value) => {
    console.log("Promise resolved with value:", value);
    return "nextnextValue";
  })
  .then((value) => {
    console.log("Promise resolved with value:", value);
  });

