<template>
  <v-app>
    <Carousel :images=imagesCarousel />
  </v-app>
</template>

<script>
  import Carousel from '@/components/Carousel.vue'

  export default {
    name: 'Home',

    data: () => ({
      imagesCarousel: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
      ]
    }),

    components: {
      Carousel,
    },
  }
</script>
