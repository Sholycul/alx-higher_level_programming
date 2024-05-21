#!/usr/bin/node

// writing to a file

const fs = require('fs');
const content = process.argv[3];

fs.writeFile(process.argv[2], content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(content);
});
