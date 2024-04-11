#!/usr/bin/node
exports.esrever = function (list) {
  // Check if list is an array
  if (!Array.isArray(list)) {
    return 'Input is not an array.';
  }

  // Initialize an empty array to store the reversed list
  const reversedList = [];

  // Iterate through the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Push each element to the reversedList array
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
