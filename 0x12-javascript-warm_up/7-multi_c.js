#!/usr/bin/node

const args = process.argv;
const n = parseInt(args[2]);

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
