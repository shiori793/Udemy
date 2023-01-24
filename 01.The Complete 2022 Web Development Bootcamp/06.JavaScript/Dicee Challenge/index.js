let randomNumber1 = Math.floor(Math.random() * 6 + 1);
let randomNumber2 = Math.floor(Math.random() * 6 + 1);
let randomDiceImg1 = "./images/dice" + randomNumber1 + ".png";
let randomDiceImg2 = "./images/dice" + randomNumber2 + ".png";
let image1 = document.querySelectorAll("img")[0];
let image2 = document.querySelectorAll("img")[1];

image1.setAttribute("src", randomDiceImg1);
image2.setAttribute("src", randomDiceImg2);

// if(randomNumber1 === 1) {
//     document.querySelector(".img1").setAttribute("src","./images/dice1.png");
// }else if(randomNumber1 === 2) {
//     document.querySelector(".img1").setAttribute("src","./images/dice2.png");
// }else if(randomNumber1 === 3) {
//     document.querySelector(".img1").setAttribute("src","./images/dice3.png");
// }else if(randomNumber1 === 4) {
//     document.querySelector(".img1").setAttribute("src","./images/dice4.png");
// }else if(randomNumber1 === 5) {
//     document.querySelector(".img1").setAttribute("src","./images/dice5.png");
// }else if(randomNumber1 === 6) {
//     document.querySelector(".img1").setAttribute("src","./images/dice6.png");
// }

// if(randomNumber2 === 1) {
//     document.querySelector(".img2").setAttribute("src","./images/dice1.png");
// }else if(randomNumber2 === 2) {
//     document.querySelector(".img2").setAttribute("src","./images/dice2.png");
// }else if(randomNumber2 === 3) {
//     document.querySelector(".img2").setAttribute("src","./images/dice3.png");
// }else if(randomNumber2 === 4) {
//     document.querySelector(".img2").setAttribute("src","./images/dice4.png");
// }else if(randomNumber2 === 5) {
//     document.querySelector(".img2").setAttribute("src","./images/dice5.png");
// }else if(randomNumber2 === 6) {
//     document.querySelector(".img2").setAttribute("src","./images/dice6.png");
// }

if(randomNumber1 > randomNumber2) {
    document.querySelector("h1").innerHTML = "Player1 Wins!";
}else if(randomNumber1 < randomNumber2) {
    document.querySelector("h1").innerHTML = "Player2 Wins!";
}else {
    document.querySelector("h1").innerHTML = "Draw";
}