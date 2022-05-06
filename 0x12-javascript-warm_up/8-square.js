#!/usr/bin/node
const process = require('process');

const num = process.argv[2];

if (isNaN(num)) {
    console.log('Missing size');
} else {
    for(let i = 0; i < num; i++) {
	let row = '';
	for(let j = 0; j < num; j++) {
            row += '#';
        }
        console.log(row+" ");
    }
}
