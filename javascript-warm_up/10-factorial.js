#!/usr/bin/node

const x = Number(process.argv[2]);

function factorial (a) {
  if (a < 0) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  if (isNaN(a)) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(x));
