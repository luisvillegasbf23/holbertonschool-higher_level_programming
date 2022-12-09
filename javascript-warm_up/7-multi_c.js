#!/usr/bin/node
// #!/usr/bin/env node
const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing number of occurences');
} else {
  for (let i = num; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
