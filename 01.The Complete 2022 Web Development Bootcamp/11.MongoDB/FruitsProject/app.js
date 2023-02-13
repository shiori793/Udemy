const { MongoClient } = require("mongodb");
// Connection URI
const uri = "mongodb://localhost:27017";
// Create a new MongoClient
const client = new MongoClient(uri);

async function run() {
  try {
    // Connect the client to the server (optional starting in v4.7)
    await client.connect();
    // Establish and verify connection
    await client.db("fruitsDB").command({ ping: 1 });
    console.log("Connected successfully to server");

    const fruitsDB = client.db("fruitsDB");
    const fruits = fruitsDB.collection("fruits");
    const doc = { name: "Apple", score: 8, review: "Good" };
    const result = await fruits.insertOne(doc);
    console.log(
    `A document was inserted with the _id: ${result.insertedId}`,
    );

  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);