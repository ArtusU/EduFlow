<template>
<div>
  <Nav />
  <router-view/>
  <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
  </footer>
</div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
    name: 'App',
    components: {
        Nav,
    }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
