<template>
  <v-app>
    <v-app-bar
      app
      color=#009688
      elevate-on-scroll
      scroll-target
    >

      <v-toolbar-title>Ejemplo Vue</v-toolbar-title>

      <v-spacer></v-spacer>

      Inicio
      Servicios
      Noticias
      Nuestro Equipo

      <v-spacer></v-spacer>

      <v-img
       max-width=90px
       src="https://www.misiontic2022.gov.co/746/channels-645_logo_misiontic.png"></v-img>

    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>

    <v-footer
    dark
    padless
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <strong class="subheading">Get connected with us on social networks!</strong>

        <v-spacer></v-spacer>

        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4"
          dark
          icon
        >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text class="py-2 white--text text-center">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-card-text>
    </v-card>
  </v-footer>

  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
  }),
};
</script>
