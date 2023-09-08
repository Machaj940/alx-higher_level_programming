#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
//const wA = "https://swapi-api.alx-tools.com/api/people/18/";

request(url, function (error, response, body) {
    const characterCount = JSON.parse(body).results.filter(value => value.characters === "https://swapi-api.alx-tools.com/api/people/18/").length;
    console.log(characterCount);
});
