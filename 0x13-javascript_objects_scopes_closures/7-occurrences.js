#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numMatches = 0;
    for (let i = 0, j = list.length; i < j; i += 1) {
        if (list[i] === searchElement) {
            numMatches += 1;
        }
    }
    return numMatches;
};
