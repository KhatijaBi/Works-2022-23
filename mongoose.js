const mongoose = require('mongoose');
const prompt = require('prompt-sync')();

const uri = 'mongodb+srv://AlishaTaj:alisha24102003@cluster0.9ugfq6w.mongodb.net/test';
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

// Define the Camel schema
const camelSchema = new mongoose.Schema({
  height: Number,
  length: Number,
  sum: Number
}, { versionKey: false });

// Create the Camel model
const Camel = mongoose.model('Camel', camelSchema);

// Create a new camel entry
async function createCamel(height, length) {
  const camels = await Camel.find();
  let sum = 0;
  camels.forEach(camel => {
    sum += camel.height + camel.length;
  });

  const camel = new Camel({
    height,
    length,
    sum: sum + height + length
  });

  await camel.save();
  console.log('Camel created successfully!');
}

// Read all camel entries
async function readCamels() {
  const camels = await Camel.find();
  console.log('Camels:', camels);
}

// Update a camel's height by ID
async function updateCamelHeight(camelId, newHeight) {
  await Camel.findByIdAndUpdate(camelId, { height: newHeight });
  console.log('Camel height updated successfully!');
}

// Delete a camel by ID
async function deleteCamel(camelId) {
  await Camel.findByIdAndDelete(camelId);
  console.log('Camel deleted successfully!');
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

  mongoose.disconnect();
}

main().catch(console.error);
