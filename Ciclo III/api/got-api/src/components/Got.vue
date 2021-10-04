<template>
    <div class="d-flex flex-wrap">
        <v-card v-if="desserts">
            <v-card-title>
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
            @click:row="mostrar"
            >
                <template v-slot:[`item.image`]="{ item }">
                    <v-img :src="item.imageUrl" :alt="item.name" max-width="100px"></v-img>
                </template>
            </v-data-table>
        </v-card>

        <v-card v-if="member">
            <v-card-title>{{ member.title }}</v-card-title>
            <v-img :src=member.imageUrl max-width="300px"></v-img>
            <v-card-text>
                <p>Nombre: {{ member.firstName }}</p>
                <p>Apellido: {{ member.lastName }}</p>
                <p>Familia: {{ member.family }}</p>
                <p>Imagen: {{ member.image }}</p>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
  import axios from "axios"

  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'ID',
            align: 'start',
            filterable: false,
            value: 'id',
          },
          { text: 'Foto', value: 'image' },
          { text: 'Nombre', value: 'firstName' },
          { text: 'Apellido', value: 'lastName' },
          { text: 'Familia', value: 'family' },
        ],
        desserts: null,
        member: null,
      }
    },
    methods: {
        mostrar(row) {
            this.member = row
        }
    },
    created () {
        axios
            .get("https://thronesapi.com/api/v2/Characters")
            .then((response) => {
                this.desserts = response.data
                console.log(response.data)
            })
    }
  }
</script>