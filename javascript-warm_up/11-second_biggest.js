#!/usr/bin/node

const Arr = Number(process.argv.slice(2));

function FindSecondLargest (a) {
  if (a.length < 2) {
    return 0;
  }

  if (isNaN(a)) {
    return 0
  }

  let largest = a[0];
  let secondLargest = -Infinity;

  for (let i = 1; i < a.length; i++) {
    if (a[i] > largest) {
      secondLargest = largest;
      largest = a[i];
    } else if (a[i] > secondLargest && a[i] !== largest) {
      secondLargest = a[i];
    }
  }

  if (secondLargest === -Infinity) {
    return 0;
  } else {
    return secondLargest;
  }
}

console.log(FindSecondLargest(Arr));
