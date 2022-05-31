#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((n, x) => n + (x === searchElement), 0);
  console.log(count);
};
