require("dotenv").config();

const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");

const port = process.env.PORT;

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended: true}));

// API Rutes
app.use('/api', require("./router/router"));

// app.get('/saludo', (request, response) => {
//   response.send({data: "Hola Tripulantes"})
// })

// DB
mongoose.connect(process.env.URI_DB)
  .then(() => console.log("Se ha establecido la conexión con la base de datos!"))
  .catch(err => console.error(err));

// Servidor
app.listen(port, () => {
  console.log(`Aplicación escuchando por http://localhost:${port}`)
})