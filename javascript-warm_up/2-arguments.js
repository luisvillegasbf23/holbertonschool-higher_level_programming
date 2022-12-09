#!/usr/bin/env node
//#!/usr/bin/node
// prints a message depending of args
if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
