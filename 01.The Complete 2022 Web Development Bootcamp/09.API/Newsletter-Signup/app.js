const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();
const https = require('https');

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/signup.html");
});

app.post("/", (req,res) => {
    const firstName = req.body.fName;
    const lastName = req.body.lName;
    const email = req.body.email;

    const data = {
        members: [
            {
                email_address: email,
                status: "subscribed",
                merge_fields: {
                    FNAME: firstName,
                    LNAME: lastName
                }
            }
        ]
    };

    const jsonData = JSON.stringify(data);

    const url = 'https://<dc>.api.mailchimp.com/3.0/lists/{list_id}/members/{subscriber_hash}/notes/{id}';

    const options = {
        method: 'POST',
        auth: 'aaa'
    };

    https.request(url, options, () => {

        if (response.statusCode = 200) {
            res.sendFile(__dirname + "/success.html");
        } else {
            res.sendFile(__dirname + "/failure.html");
        }

        response.on('data', (data) => {
            console.log(JSON.parse(data));
        });
    });

    request.write(jsonData);
    request.send();

    // const client = require("@mailchimp/mailchimp_marketing");

    // client.setConfig({
    // apiKey: "YOUR_API_KEY",
    // server: "YOUR_SERVER_PREFIX",
    // });

    // const run = async () => {
    // const response = await client.lists.createList({
    //     name: "name",
    //     permission_reminder: "permission_reminder",
    //     email_type_option: true,
    //     contact: {
    //         company: "company",
    //         address1: "address1",
    //         city: "city",
    //         country: "country",
    //     },
    //     campaign_defaults: {
    //         from_name: "from_name",
    //         from_email: "Beulah_Ryan@hotmail.com",
    //         subject: "subject",
    //         language: "language",
    //     },
    // });
    // console.log(response);
    // };

    // run();
});

app.get("/failure", (req, res) => {
    res.sendFile(__dirname + "/failure.html");
})

app.listen(process.env.PORT, () => {
    console.log("Server is running on port 3000.");
});