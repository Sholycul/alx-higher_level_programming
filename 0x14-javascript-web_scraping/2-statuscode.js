#!/usr/bin/node

// Using request get method

const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code : ${response.statusCode}`);
});
