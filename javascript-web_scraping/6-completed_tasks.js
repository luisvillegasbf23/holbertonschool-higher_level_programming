#!/usr/bin/env node
// #!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

function bar (err, resp, body) {
   if (!err) {
    const completed = {};
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (completed[todos[i].userId] === undefined) {
          completed[todos[i].userId] = 0;
        }
        completed[todos[i].userId]++;
      }
    }
    console.log(completed);
  }
}

request(URL, bar);
