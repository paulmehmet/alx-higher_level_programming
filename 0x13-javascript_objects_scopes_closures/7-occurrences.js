#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce(
    (occurence, item) => (item === searchElement ? occurence + 1 : occurence),
    0
  );
};
