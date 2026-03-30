#!/usr/bin/node

const x = Number(process.argv[2]);
const y = Number(process.argv[3]);

function add (a, b) {
  if (a === undefined || b === undefined) {
    console.log('NaN');
  }
  return a + b;
}

console.log(add(x, y));
