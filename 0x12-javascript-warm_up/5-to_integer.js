#!/usr/bin/node
const process = require('process');

const result = Math.floor(Number(process.argv[2]));

if (isNaN(result)) {
    console.log('Not a number');
} else {
    console.log(`My number: ${result}`);
}
