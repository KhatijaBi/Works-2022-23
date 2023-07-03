const { MongoClient } = require("mongodb");
// Replace the uri string with your MongoDB deployment's connection string.
const uri =
"mongodb+srv://AlishaTaj:alisha24102003@cluster0.9ugfq6w.mongodb.net/?retryWrites=true&w=majority";

const client = new MongoClient(uri);
async function run() {
  try {
    await client.connect();
    const coll = client.db("sample_airbnb").collection("listingsAndReviews");

    // find code goes here
    let cursor = coll.find();

    await cursor.forEach(console.log);
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);
