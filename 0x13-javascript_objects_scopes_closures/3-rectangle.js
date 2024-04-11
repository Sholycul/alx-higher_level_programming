#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let result = '';
      for (let i = 0; i < this.width; i++) {
        result += 'X';
      }
      console.log(result);
    }
  }
};
