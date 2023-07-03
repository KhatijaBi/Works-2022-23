
const { MongoClient, ServerApiVersion } = require('mongodb');
const mongoose = require('mongoose');
main().catch(err => console.log(err));

async function main() {
   await mongoose.connect("mongodb+srv://AlishaTaj:alisha24102003@cluster0.9ugfq6w.mongodb.net/test");

const kittySchema = new mongoose.Schema({
    name: String
  })

kittySchema.methods.speak = function speak() {
    const greeting = this.name
      ? 'Meow name is ' + this.name
      : 'I don\'t have a name';
    return console.log(greeting);
  }
const kitten=new mongoose.model("kitten",kittySchema);

const silence = new kitten({ name: 'Silence' });
await silence.save();
console.log(silence.name); // 'Silence'

const fluffy = new kitten({ name: 'fluffy' });
fluffy.speak(); // "Meow name is fluffy"

const silence1 = new kitten({ name: 'Silence1' });
await silence1.save();

const kittens = await kitten.find();
console.log(kittens);

await kitten.find({ name: /^fluff/ });
await fluffy.save();
}