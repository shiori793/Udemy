const express = require("express");
const app = express();

app.get("/", function(req, res) {
    res.send("<h1>Hello, world</h1>");
});

app.get("/contact", function(req, res) {
    res.send("Contact me at: shiori@mail.com");
});

app.get("/about", function(req, res) {
    res.send("My name is Shiori");
});

app.get("/hobby", function(req, res) {
    res.send("<ul><li>Figure skating</li><li>Japanese Calligraphy</li></ul>")
})

app.listen(3000, function() {
    console.log("Server started on port 3000");
});