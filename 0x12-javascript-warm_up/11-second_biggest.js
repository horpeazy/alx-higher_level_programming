#!/usr/bin/node

const myArray = [];

if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    myArray.push(parseInt(process.argv[i]));
  }
  myArray.sort();
  console.log(myArray[myArray.length - 2]);
}
