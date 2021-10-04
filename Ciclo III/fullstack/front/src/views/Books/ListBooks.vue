<template>
  <v-card>
    <v-btn @click="guardar">Guardar Libro</v-btn>
    <v-card-title>
      Libros
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script>
  import {
    getAllBooks,
    insertBook
  } from "../../services/BooksServices";

  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'ISBN',
            align: 'start',
            value: 'isbn',
          },
          { text: 'Titulo', value: 'titulo' },
          { text: 'Año', value: 'anio' },
          { text: 'Genero', value: 'genero' },
          { text: 'Autores', value: 'autores' },
        ],
        desserts: [],
      }
    },
    mounted () {
      getAllBooks()
        .then((response) => {
          this.desserts = response.data;
        })
        .catch((err) => console.error(err));
    },
    methods: {
      guardar () {
        const book = {
          isbn: "sdfsdfsdf",
          titulo: "Nuevo libro",
          anio: "2021",
          autores: ["Autor"],
          genero: "sgfdsdfgs"
          }
          insertBook(book)
      }
    }
  }
  
</script>