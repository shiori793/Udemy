const express = require('express');
const bodyParser = require('body-parser');
const date = require(__dirname + "/date.js");

const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

const items = ['Buy Food', 'Cook Food', 'Eat Food'];
const workItems = [];

app.get("/", (req, res) => {

    let day = date.getDate();

    // let today = new Date();
    // let currentDay = today.getDay();
    // let day = "";

    // if (currentDay === 6 || currentDay === 0) {
        // day = "weekend";
        // res.write("<h1>Yay, It's the weekend!</h1>");
    // } else {
        // day = "weekday";
        // res.write("<p>It is not the weekend</p>");
        // res.write("<h1>Boo! I have to work.</h1>");
        // res.sendFile(__dirname + "/index.html");
    // }

    // switch (currentDay) {
    //     case 0:
    //         day = "Sunday";
    //         break;

    //     case 1:
    //         day = "Monday";
    //         break;
        
    //     case 2:
    //         day = "Tuesday";
    //         break;
        
    //     case 3:
    //         day = "Wednesday";
    //         break;
        
    //     case 4:
    //         day = "Thursday";
    //         break;
        
    //     case 5:
    //         day = "Friday";
    //         break;
        
    //     case 6:
    //         day = "Saturday";
    //         break;
    
    //     default:
    //         console.log('Error: current day is equal to :' + currentDay);
    //         break;
    // }
    res.render("list", {listTitle: day, newListItems: items});
    // res.send();

});

app.post('/',(req, res) => {
    let item = req.body.newItem;
    if (req.body.button === "Work") {
        workItems.push(item);
        res.redirect("/work");
    } else {
        items.push(item);
        res.redirect('/');
    }
});

app.get("/work", (req, res) => {
    res.render("list", {listTitle: "Work List", newListItems: workItems});
});

app.get("/about", (req, res) => {
    res.render("about");
})

app.listen(3000, () => {
    console.log("Server is running on port 3000.");
});