#!/usr/bin/node
// the second biggest integer in the list of arguments.

const numsArray = process.argv.slice(2);
function secondBig (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return (array.pop());
  }
}
console.log(secondBig(numsArray));
