#!/usr/bin/node

const Arg = process.argv.slice(2);

if (Arg.length === 1) {
  console.log('Argument found');
} else if (Arg.length >= 2) {
  console.log('Arguments found');
} else if (Arg.length === 0) {
  console.log('No argument');
}
