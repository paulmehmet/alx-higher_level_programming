#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
const keys = Object.keys(dict);
const vals = Object.values(dict);
const uniqVals = [...new Set(vals)];
console.log(uniqVals);

for (const [key, value] of Object.entries(dict)) {
  if (value in uniqVals) {
    console.log(key);
  }
}
