#!/usr/bin/node
// #!/usr/bin/env node
// File System Object

const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');
function bar (err, data) {
  err ? console.log(err) : console.log(data);
}

// (file, encoding, function)
fs.writeFile(file, str, 'utf-8', bar);
// fs.readFile(file, 'utf-8', bar);
