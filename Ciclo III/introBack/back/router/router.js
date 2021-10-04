const express = require("express");

const ExampleController = require("../controllers/ExampleController");
const CustomersController = require("../controllers/CustomersController");

const router = express.Router();

// Rutes
// router.get('/', (request, response) => {
//   response.send("Acabas de hacerme una solicitud!");
// })
router.get('/', ExampleController.entrada);

// router.get('/saludo', (request, response) => {
//   response.status(200).json({saludo: "Hola Tripulantes!"});
// })
router.get('/saludo', ExampleController.saludar);

// Rutes Customers
router.get('/customers/all', CustomersController.getAll);
router.get('/customers/:id', CustomersController.getById);
router.get('/customers/address/:address', CustomersController.getByAddress);
router.get('/customers/:name/:address', CustomersController.getByNameAddress);
router.post('/customers/', CustomersController.insert);
router.delete('/customers/:id', CustomersController.deleteById);
router.put('/customers/:id', CustomersController.updateById);

// Rutes Transactions
// router.get('/transactions/all', TransactionsController.getAll);

module.exports = router;