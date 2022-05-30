#!/usr/bin/node
const process = require('process');

if (isNaN(process.argv[2])) {
  console.log(1);
} else if (process.argv[2] === 0) {
  console.log(1);
} else {
  let fact = 1;
  for (let i = 1; i <= process.argv[2]; i++) {
    fact *= i;
  }
    console.log(fact);
}
