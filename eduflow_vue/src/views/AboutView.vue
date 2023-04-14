<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">About</h1>
      </div>
    </div>
    <section class="section">
      <div class="hero-body has-text-centered">
        <h3 class="text">EduFlow is a Learning Management System (LMS) that delivers a dynamic and immersive learning experience. </h3>
        <h3 class="text">Our platform is built with state-of-the-art technology, powered by the Django Rest Framework at the back end and Vue.js at the front end.</h3>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  mounted() {
    document.title = 'About | EduFlow'
  }
}
</script>