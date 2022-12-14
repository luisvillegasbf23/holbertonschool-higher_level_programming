#!/usr/bin/node
// #!/usr/bin/env node

const ID = process.argv[2];
const request = require('request');
const URL = `https://swapi-api.hbtn.io/api/films/${ID}`;

function bar (err, resp, body) {
  console.log(err || JSON.parse(body).title);
}

request(URL, bar);
