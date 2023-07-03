const prompt = require('prompt-sync')();

class Camel {
  constructor(height, length) {
    this.height = height;
    this.length = length;
  }
}

class CamelFarm {
  constructor() {
    this.camels = [];
  }

  addCamel(camel) {
    this.camels.push(camel);
  }

  getTotalHeight() {
    let totalHeight = 0;
    for (let camel of this.camels) {
      totalHeight += camel.height;
    }
    return totalHeight;
  }

  getTotalLength() {
    let totalLength = 0;
    for (let camel of this.camels) {
      totalLength += camel.length;
    }
    return totalLength;
  }
}

function main() {
  let n = parseInt(prompt("How many camels do you have? "));
  let camelFarm = new CamelFarm();

  for (let i = 0; i < n; i++) {
    let height = parseFloat(prompt(`Enter the height of camel ${i + 1}: `));
    let length = parseFloat(prompt(`Enter the length of camel ${i + 1}: `));
    let camel = new Camel(height, length);
    camelFarm.addCamel(camel);
  }

  let totalHeight = camelFarm.getTotalHeight();
  let totalLength = camelFarm.getTotalLength();

  console.log(`The total height of the camels is: ${totalHeight}`);
  console.log(`The total length of the camels is: ${totalLength}`);
}

main();
