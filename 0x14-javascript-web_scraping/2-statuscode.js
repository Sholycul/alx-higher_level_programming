#!/usr/bin/node

// Using request get method

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
