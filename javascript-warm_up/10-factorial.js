#!/usr/bin/node
// factorial.

const arg = parseInt(process.argv[2]);
function factorial (arg) {
  if (!arg || arg === 0) {
    return (1);
  }
  return (arg * factorial(arg - 1));
}
console.log(factorial(arg));
