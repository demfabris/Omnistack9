const express = require('express');
const multer = require('multer');
const uploadConfig = require('./config/upload.js');

//CONTROLERS

const SpotController = require('./controllers/SpotController');
const SessionController = require('./controllers/SessionController');
const DashboardController = require('./controllers/DashboardController');
const BookingController = require('./controllers/BookingController');

//INIT VARS

const routes = express.Router();
const upload = multer(uploadConfig);

//ROUTES

routes.post('/sessions', SessionController.store);
routes.get('/spots', SpotController.index);
routes.post('/spots', upload.single('thumbnail'),SpotController.store);
routes.get('/dashboard', DashboardController.show);
routes.post('/spots/:spot_id/bookings', )

module.exports = routes;
