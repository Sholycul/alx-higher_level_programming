#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      return num.toString(base);
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base).toString(base);
    }
  };
};
