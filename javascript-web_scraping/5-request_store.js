#!/usr/bin/node
// #!/usr/bin/env node

const request = require('request');
const URL = process.argv[2]
const FILE = process.argv[3]
const fs = require('fs');

function bar (err, resp, body) {
  if (err == null) {
    fs.writeFileSync(FILE, body);
  }
}

request(URL, bar);
