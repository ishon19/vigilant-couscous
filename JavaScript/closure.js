function test() {
  let num = 1;
  function test2() {
    return num++;
  }
  return test2;
}

const func = test();

console.log(func()); // prints 1
console.log(func()); // prints 2
