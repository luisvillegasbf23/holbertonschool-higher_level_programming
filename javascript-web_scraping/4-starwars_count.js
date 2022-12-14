#!/usr/bin/node
// #!/usr/bin/env node

const URL = process.argv[2];
const request = require('request');
let films = 0;

function bar (err, resp, body) {
  if (err == null) {
    const completed = JSON.parse(body);
    const results = completed.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          films++;
        }
      }
    }
  }
  console.log(films);
}

request(URL, bar);
