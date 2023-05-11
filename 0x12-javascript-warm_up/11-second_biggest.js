#!/usr/bin/node
const process = require('process');

const argArray = [...new Set(process.argv)];

if (argArray) {
    newArray = argArray.slice(2);
    result = newArray.sort(function(a, b) { return b - a})[1];
    console.log(result);
}
else {
    console.log(0);
}
