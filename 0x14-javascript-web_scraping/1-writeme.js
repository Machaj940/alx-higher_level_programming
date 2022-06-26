#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const content = process.argv[3];

fs.writeFile(process.argv[2], content, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
