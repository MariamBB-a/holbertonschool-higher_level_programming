#!/usr/bin/node

const myNumber = process.argv[2];

if (!isNaN(myNumber)) {
  console.log(`My number: ${parseInt(myNumber)}`);
} else {
  console.log('Not a number');
}
