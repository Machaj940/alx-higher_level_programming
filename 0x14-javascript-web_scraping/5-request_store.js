#!/usr/bin/node

const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
