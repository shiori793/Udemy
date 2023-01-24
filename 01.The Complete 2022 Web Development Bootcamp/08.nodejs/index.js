// const fs = require("fs");
// fs.copyFileSync("file1.txt", "file2.txt");

let superheroes = require("superheroes");
let supervillains = require("supervillains");

let mySuperheroName = superheroes.random();
let mySupervillainName = supervillains.random();

console.log(mySuperheroName);
console.log(mySupervillainName);