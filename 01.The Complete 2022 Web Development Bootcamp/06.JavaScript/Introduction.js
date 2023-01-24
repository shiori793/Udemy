// let name = prompt("What is you name?");
// let firstChar = name.slice(0,1);
// let upperCaseFirstChar = firstChar.toUpperCase();
// let restName = name.slice(1,name.length);
// let fullName = upperCaseFirstChar + restName;
// alert("Hello, " + fullName);


function getMilk(money) {   
    console.log("leaveHouse");
    console.log("moveRight");
    console.log("moveRight");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveRight");
    console.log("moveRight");

    let bottle = Math.floor(money / 1.5);
    console.log("buy " + bottle + " bottles of milk");

    console.log("moveLeft");
    console.log("moveLeft");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveLeft");
    console.log("moveLeft");
    console.log("enterHouse");
}

getMilk(30);
getMilk(40);