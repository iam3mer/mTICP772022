const mongoose = require("mongoose");

const booksSchema = mongoose.Schema({
  isbn: String,
  titulo: String,
  anio: String,
  autores: Array,
  genero: String
})

module.exports = mongoose.model("books", booksSchema);