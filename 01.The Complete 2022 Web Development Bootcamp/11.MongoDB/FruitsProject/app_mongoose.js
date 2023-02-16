const mongoose = require('mongoose');
mongoose.set('strictQuery', true);
mongoose.connect('mongodb://localhost:27017/fruitsDB', { useNewUrlParser: true });

// const fruitSchema = new mongoose.Schema ({
//   name: String,
//   rating: Number,
//   review: String
// });

const fruitSchema = new mongoose.Schema ({
  name: {
    type: String,
    required: [true, "Please check your data entry."]
  },
  rating: {
    type: Number,
    min: 1,
    max: 10
  },
  review: String
});

const Fruit = mongoose.model("Fruit", fruitSchema);

// const fruit = new Fruit({
//   name: "Apple",
//   rating: 10,
//   review: "Pretty solid as a fruit"
// })

// fruit.save();

const personSchema = new mongoose.Schema ({
  name: String,
  age: Number,
  favouriteFruit: fruitSchema
})

const Person = mongoose.model("Person", personSchema);

const pineapple = new Fruit({
  name: "Pineapple",
  rating: 9,
  review: "Great Fruit"
})

pineapple.save();

const person = new Person({
  name: "Amy",
  age: 12,
  favouriteFruit: pineapple
})

person.save();

// Person.deleteOne({name: "Amy"}, function(err) {
//   if (err) {
//     console.log(err);
//   }
// })

// const kiwi = new Fruit({
//   name: "Kiwi",
//   rating: 10,
//   review: "The best fruits!"
// })

// const orange = new Fruit({
//   name: "Orange",
//   rating: 4,
//   review: "Too sour for me"
// })

// const banana = new Fruit({
//   name: "Banana",
//   rating: 3,
//   review: "Weird texture"
// })

// Fruit.insertMany([kiwi, orange, banana], function(err){
//   if (err) {
//     console.log(err);
//   } else {
//     console.log("Successfully saved all fruits.");
//   }
// })

Fruit.find(function(err, fruits) {
  if (err) {
    console.log(err);
  } else {
    mongoose.connection.close();
    fruits.forEach( fruit => {
      console.log(fruit.name);
    })
  }
})

// Fruit.updateOne({_id: "63ed552b85f38ba34e247015"}, {rating: 5}, function(err){
//   if (err) {
//     console.log(err);
//   }else {
//     console.log("Successfully updated.");
//   }
// })

// Fruit.deleteOne({name: 'Banana'}, function(err) {
//   if(err) {
//     console.log(err);
//   } else {
//     console.log("successfully deleted");
//   }
// })