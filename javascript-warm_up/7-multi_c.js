#!/usr/bin/node

let x = process.argv[2];
const myString = 'C is fun';

if (!isNaN(x)) {
  x = parseInt(x);
} else {
  console.log('Missing number of occurrences');
}
if (x > 0) {
  while (x > 0) {
    console.log(myString);
    x--;
  }
}
