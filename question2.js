const prompt = require('prompt-sync')();
const { MongoClient } = require('mongodb');

const uri = 'mongodb+srv://AlishaTaj:alisha24102003@cluster0.9ugfq6w.mongodb.net/?retryWrites=true&w=majority'; // Update with your MongoDB connection URI
const client = new MongoClient(uri);

class Shop {
  constructor(name, rent) {
    this.name = name;
    this.rent = rent;
  }
}

class NShops {
  constructor(collection) {
    this.collection = collection;
  }

  async addShop(shop) {
    await this.collection.insertOne(shop);
    console.log('Shop added successfully.');
  }

  async getAllShops() {
    const shops = await this.collection.find().toArray();
    console.log('All Shops:');
    console.log(shops);
  }

  async updateShop(name, rent) {
    await this.collection.updateOne({ name: name }, { $set: { rent: rent } });
    console.log(`Shop "${name}" updated successfully.`);
  }

  async deleteShop(name) {
    await this.collection.deleteOne({ name: name });
    console.log(`Shop "${name}" deleted successfully.`);
  }

  async getTotalRents() {
    const shops = await this.collection.find().toArray();
    let totalRents = 0;
    for (let shop of shops) {
      totalRents += shop.rent;
    }
    return totalRents;
  }
}

async function main() {
  try {
    await client.connect();
    const database = client.db('shopping_complex');
    const collection = database.collection('shops');
    let shoppingComplex = new NShops(collection);

    // Prompt the user for shop data
    let shopCount = parseInt(prompt("Enter the number of shops in the complex: "));
    for (let i = 0; i < shopCount; i++) {
      let name = prompt(`Enter the name of shop ${i + 1}: `);
      let rent = parseFloat(prompt(`Enter the rent of ${name} shop: `));
      let shop = new Shop(name, rent);
      await shoppingComplex.addShop(shop);
    }

    let totalRents = await shoppingComplex.getTotalRents();

    console.log(`The total rents in the shopping complex is: ${totalRents}`);

    // Perform CRUD operations
    console.log('Performing CRUD operations:');

    // Get all shops
    await shoppingComplex.getAllShops();

    // Update a shop
    let updateName = prompt('Enter the name of the shop to update: ');
    let newRent = parseFloat(prompt('Enter the new rent for the shop: '));
    await shoppingComplex.updateShop(updateName, newRent);

    // Delete a shop
    let deleteName = prompt('Enter the name of the shop to delete: ');
    await shoppingComplex.deleteShop(deleteName);
  } catch (error) {
    console.error('Error:', error);
  } finally {
    await client.close();
  }
}

main();
