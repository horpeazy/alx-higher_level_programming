#!/usr/bin/node
const dict = require("./101-data.js").dict;
const newDict = {};

for (let [key, value] of Object.entries(dict)) {
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
