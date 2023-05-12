#!/usr/bin/node

const list = require('./100-data.js').list;

const newArray = list.map((element, index) => element * index);
console.log(list);
console.log(newArray);
