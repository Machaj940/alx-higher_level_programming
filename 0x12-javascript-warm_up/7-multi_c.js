#!/usr/bin/node
const process = require('process');

const str = 'C is fun';

const x = Number(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
