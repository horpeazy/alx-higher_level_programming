#!/usr/bin/node
const SquareObject = require("./5-square.js");

class Square extends SquareObject {
  charPrint (character) {
    if (character) {
      for (let i = 0; i < this.height; i++) {
        let line = "";
        for (let j = 0; j < this.width; j++) {
          line += character;
	}
        console.log(line);
      }
    }
    else {
      this.print();
    }
  }
}

module.exports = Square;
