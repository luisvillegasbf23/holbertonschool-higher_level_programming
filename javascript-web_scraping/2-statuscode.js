#!/usr/bin/node
// #!/usr/bin/env node

const URL = process.argv[2];
const request = require('request');

function bar (err, resp) {
  err ? console.log(err) : console.log(`code: ${resp.statusCode}`);
}

request(URL, bar);
