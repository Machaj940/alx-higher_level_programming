#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const allCharacters = JSON.parse(body).characters;

    for (const i in allCharacters) {
      request(allCharacters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
      });
    }
  }
});
