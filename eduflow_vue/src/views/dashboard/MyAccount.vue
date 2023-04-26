<template>
    <div class="about">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">My Account</h1>
        </div>
      </div>
      <section class="section">
        <div class="columns is-multiline">
          <div class="column is-12">
            <h2 class="subtitle is-size-3">Your active courses</h2>
          </div>
          <div class="column is-4">
            CourseItem
          </div>
        </div>
        <button @click="logout()" class="button is-danger">Log out</button>
      </section>
    </div>
  </template>
  

<script>
import axios from 'axios'
export default {
  methods: {
    logout() {
      console.log("logout")

      axios.defaults.headers.common['Authorization'] = ""
      localStorage.removeItem('token')
      this.$store.commit('removeToken')
      this.$router.push('/')
    }
  }
}
</script>