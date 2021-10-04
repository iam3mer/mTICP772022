<template>
  <div class="home">
    <Api/>
  </div>
</template>

<script>
// @ is an alias to /src
import Api from '@/components/Api.vue'

export default {
  name: 'Home',
  components: {
    Api,
  }
}
</script>
