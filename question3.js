const mongoose = require('mongoose');
const prompt = require('prompt-sync')();

const uri = 'mongodb+srv://AlishaTaj:alisha24102003@cluster0.9ugfq6w.mongodb.net/?retryWrites=true&w=majority'; // Update with your MongoDB connection URI

// Define the shop schema
const shopSchema = new mongoose.Schema({
  name: String,
  rent: Number,
});

// Create the shop model
const Shop = mongoose.model('Shop', shopSchema);

async function addShops() {
  await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  const shopCount = parseInt(prompt("Enter the number of shops in the complex: "));
  for (let i = 0; i < shopCount; i++) {
    const name = prompt(`Enter the name of shop ${i + 1}: `);
    const rent = parseFloat(prompt(`Enter the rent of ${name} shop: `));
    const shop = new Shop({ name, rent });
    await shop.save();
    console.log(`Shop "${name}" added successfully.`);
  }

  mongoose.disconnect();
}

async function getAllShops() {
  await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  const shops = await Shop.find();
  console.log('All Shops:');
  console.log(shops);

  mongoose.disconnect();
}

async function updateShopRent() {
  await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  const name = prompt('Enter the name of the shop to update: ');
  const shop = await Shop.findOne({ name });
  if (shop) {
    const newRent = parseFloat(prompt('Enter the new rent for the shop: '));
    shop.rent = newRent;
    await shop.save();
    console.log(`Rent for shop "${name}" updated successfully.`);
  } else {
    console.log(`Shop "${name}" not found.`);
  }

  mongoose.disconnect();
}

async function deleteShop() {
  await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  const name = prompt('Enter the name of the shop to delete: ');
  const deleteResult = await Shop.deleteOne({ name });
  if (deleteResult.deletedCount > 0) {
    console.log(`Shop "${name}" deleted successfully.`);
  } else {
    console.log(`Shop "${name}" not found.`);
  }

  mongoose.disconnect();
}

async function main() {
  try {
    // Add shops
    await addShops();

    // Get all shops
    await getAllShops();

    // Update shop rent
    await updateShopRent();

    // Delete shop
    await deleteShop();
  } catch (error) {
    console.error('Error:', error);
  } finally {
    mongoose.disconnect();
  }
}

main();
