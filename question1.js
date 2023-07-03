const prompt = require('prompt-sync')();

class Shop {
  constructor(name, rent) {
    this.name = name;
    this.rent = rent;
  }
}

class NShops {
  constructor() {
    this.shops = [];
  }

  addShop(shop) {
    this.shops.push(shop);
  }

  getTotalRents() {
    let totalRents = 0;
    for (let shop of this.shops) {
      totalRents += shop.rent;
    }
    return totalRents;
  }
}

function main() {
  let shoppingComplex = new NShops();

  // Prompt the user for shop data
  let shopCount = parseInt(prompt("Enter the number of shops in the complex: "));
  for (let i = 0; i < shopCount; i++) {
    let name = prompt(`Enter the name of shop ${i + 1}: `);
    let rent = parseFloat(prompt(`Enter the rent of ${name} shop: `));
    let shop = new Shop(name, rent);
    shoppingComplex.addShop(shop);
  }

  let totalRents = shoppingComplex.getTotalRents();

  console.log(`The total rents in the shopping complex is: ${totalRents}`);
}

main();
