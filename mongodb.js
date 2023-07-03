const { MongoClient } = require('mongodb');
const prompt = require('prompt-sync')();

const uri = ('mongodb+srv://AlishaTaj:alisha24102003@cluster0.9ugfq6w.mongodb.net/test');
const dbName = 'camelFarm'; // Database name

async function createCamel(height, length) {
  const client = new MongoClient(uri);
  try {
    await client.connect();
    const db = client.db(dbName);
    const camelCollection = db.collection('camels');
    const camel = { height, length };
    await camelCollection.insertOne(camel);
    console.log('Camel created successfully!');
  } finally {
    client.close();
  }
}

async function readCamels() {
  const client = new MongoClient(uri);
  try {
    await client.connect();
    const db = client.db(dbName);
    const camelCollection = db.collection('camels');
    const camels = await camelCollection.find().toArray();
    console.log('Camels:', camels);
  } finally {
    client.close();
  }
}

async function updateCamelHeight(camelId, newHeight) {
  const client = new MongoClient(uri);
  try {
    await client.connect();
    const db = client.db(dbName);
    const camelCollection = db.collection('camels');
    await camelCollection.updateOne({ _id: camelId }, { $set: { height: newHeight } });
    console.log('Camel height updated successfully!');
  } finally {
    client.close();
  }
}

async function deleteCamel(camelId) {
  const client = new MongoClient(uri);
  try {
    await client.connect();
    const db = client.db(dbName);
    const camelCollection = db.collection('camels');
    await camelCollection.deleteOne({ _id: camelId });
    console.log('Camel deleted successfully!');
  } finally {
    client.close();
  }
}

async function main() {
  let n = parseInt(prompt('How many camels do you have? '));

  // Create camel entries
  for (let i = 0; i < n; i++) {
    let height = parseFloat(prompt(`Enter the height of camel ${i + 1}: `));
    let length = parseFloat(prompt(`Enter the length of camel ${i + 1}: `));
    await createCamel(height, length);
  }

  // Read all camel entries
  await readCamels();

  // Update a camel's height
  let camelIdToUpdate = prompt('Enter the ID of the camel to update its height: ');
  let newHeight = parseFloat(prompt('Enter the new height: '));
  await updateCamelHeight(camelIdToUpdate, newHeight);

  // Delete a camel
  let camelIdToDelete = prompt('Enter the ID of the camel to delete: ');
  await deleteCamel(camelIdToDelete);

  // Read all camel entries again
  await readCamels();
}

main().catch(console.error);
