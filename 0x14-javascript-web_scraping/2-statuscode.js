#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});


/* OR
request.get(url).on('response', function(response) {
    console.log("code: " + response.statusCode);
});
*/
