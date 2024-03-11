#!/usr/bin/node
// script that writes string to a file
const { writeFile } = require('fs');
const { argv } = require('process');

writeFile(`${argv[2]}`, argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
