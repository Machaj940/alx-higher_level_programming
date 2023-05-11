#!/usr/bin/node
const process = require('process');

if (process.argv.length > 1) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
