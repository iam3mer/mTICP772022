<template>
  <v-carousel hide-delimiters>
    <v-carousel-item
      v-for="(img,i) in images"
      :key="i"
      :src="img.src"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
          //
      }
    },
    props: [
        'images'
    ]
  }
</script>

<style>

</style>