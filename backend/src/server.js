const express = require('express');
const mongoose = require('mongoose');
const routes = require('./routes.js');
const app = express();

mongoose.connect('mongodb+srv://omnistack:omnistack@omnistack9-nqvfe.mongodb.net/semana09?retryWrites=true&w=majority',
    {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    }
);

//req.query =
//req.params = 
//req.body = 


app.use(express.json());
app.use(routes);
app.listen(3333);
