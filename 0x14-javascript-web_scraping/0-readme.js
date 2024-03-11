#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
const process = require('process');

fs.readFile(`${process.argv[2]}`, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
