#!/usr/bin/node
// task 6

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
