#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let myRow = '';
      for (let j = 0; j < this.width; j++) {
        myRow += c;
      }
      console.log(myRow);
    }
  }
}

module.exports = Square;
