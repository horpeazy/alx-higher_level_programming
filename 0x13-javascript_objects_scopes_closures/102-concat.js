#!/usr/bin/node
const fs = require('fs');

try {
  const data1 = fs.readFileSync(process.argv[2], 'utf-8');
  const data2 = fs.readFileSync(process.argv[3], 'utf-8');
  fs.writeFile(process.argv[4], data1 + data2, function (error) {
    if (error) {
      throw (error);
    }
  });
} catch (error) {
  console.error(error);
}
