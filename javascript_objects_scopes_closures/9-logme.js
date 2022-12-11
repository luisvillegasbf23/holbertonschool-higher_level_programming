#!/usr/bin/node
// task 9

let count = -1;
exports.logMe = function (item) {
  count++;
  console.log(count + ': ' + item);
};
