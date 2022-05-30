#!/usr/bin/node
const process = require('process');

function factorial (x) {
  if (isNaN(x) || x === 0 || x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

console.log(factorial(process.argv[2]));
