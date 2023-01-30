const express = require('express');
const https = require('https');
const app = express();
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({extended: true}));

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
})

app.post("/", (req, res) => {
    let cityName = req.body.cityName;
    let days = '3';

    const options = {
        "method": "GET",
        "hostname": "weatherapi-com.p.rapidapi.com",
        "port": null,
        "path": "/forecast.json?q=" + cityName + "&days=" + days,
        "headers": {
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
            "useQueryString": true
        }
    };

    const request = https.request(options, async function (response) {
        const chunks = [];
                
            response.on("data", function (chunk) {
                chunks.push(chunk);
            });
                
            response.on("end", function () {
                const body = Buffer.concat(chunks);
                let weatherData = JSON.parse(body.toString());
                let condition = weatherData.current.condition.text;
                let temperature = weatherData.current.temp_c;
                let icon = weatherData.current.condition.icon;
                res.write("<p>Current weather is " + condition + "<p>");
                res.write("<img src='" + icon + "' />");
                res.write("<h1>Current temperature in " + cityName + " is " + temperature + " degree Celcius.</h1>");
                res.send();
                // res.send(weatherData);
                });
            
            response.on("error", () => {
                console.log("error");
            });
        });
    request.end();
});

// app.get("/", (req, res) => {

//     // const url ='https://weatherapi-com.p.rapidapi.com/forecast.json';

//     // https.get(url, options, (response) => {
//     //     console.log(response.statusCode);
//     //     response.on('data', (data) => {
//     //         console.log(data);
//     //         const weatherData = JSON.parse(data);
//     //         console.log(weatherData);

//     //         // const temp = weatherData.main.temp;
//     //     });
//     // }).on('error', (e) => {
//     //     console.error(e);
//     // });

//     const request = https.request(options, async function (response) {
//         const chunks = [];
        
//         response.on("data", function (chunk) {
//             chunks.push(chunk);
//         });
        
//         response.on("end", function () {
//             const body = Buffer.concat(chunks);
//             // console.log(body.toString());
//             let weatherData = JSON.parse(body.toString());
//             let condition = weatherData.current.condition.text;
//             let temperature = weatherData.current.temp_c;
//             let icon = weatherData.current.condition.icon;
//             res.write("<p>Current weather is " + condition + "<p>");
//             res.write("<img src='" + icon + "' />");
//             res.write("<h1>Current temperature in Vancouver is " + temperature + " degree Celcius.</h1>");
//             res.send();
//             // res.send(weatherData);
//         });
    
//         response.on("error", () => {
//             console.log("error");
//         });
//     });
//     request.end();
// })

app.listen(3000, () => {
    console.log('Server is running on port 3000.');
});