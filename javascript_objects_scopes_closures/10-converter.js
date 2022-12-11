#!/usr/bin/node
// task 10

exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};
