#!/usr/bin/node
// script that prints out the status code from a  GET request
const { argv } = require('process');
const request = require('request');

const URL = argv[2];
request(URL, (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`code: ${res.statusCode}`);
});
