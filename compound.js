const prompt = require('prompt-sync')();

class Fraction {
  constructor(numerator, denominator) {
    this.numerator = numerator;
    this.denominator = denominator;
  }

  add(fraction) {
    let numerator = this.numerator * fraction.denominator + fraction.numerator * this.denominator;
    let denominator = this.denominator * fraction.denominator;
    return new Fraction(numerator, denominator);
  }
}

class CompoundFraction {
  constructor() {
    this.fractions = [];
  }

  addFraction(fraction) {
    this.fractions.push(fraction);
  }

  getCompoundFraction() {
    let result = new Fraction(0, 1);
    for (let fraction of this.fractions) {
      result = result.add(fraction);
    }
    return result;
  }
}

function main() {
  let n = parseInt(prompt("How many fractions do you want to compound? "));
  let compoundFraction = new CompoundFraction();

  for (let i = 0; i < n; i++) {
    let numerator = parseInt(prompt(`Enter numerator for fraction ${i + 1}: `));
    let denominator = parseInt(prompt(`Enter denominator for fraction ${i + 1}: `));
    let fraction = new Fraction(numerator, denominator);
    compoundFraction.addFraction(fraction);
  }

  let result = compoundFraction.getCompoundFraction();
  let wholeNumber = Math.floor(result.numerator / result.denominator);
  console.log(`The compound fraction is: ${wholeNumber}`);
}

main();
