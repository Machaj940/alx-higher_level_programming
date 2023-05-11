#!/usr/bin/node
const process = require('process');

function add(a, b) {
    console.log(a + b);
}

add(Number(process.argv[2]), Number(process.argv[3]));
