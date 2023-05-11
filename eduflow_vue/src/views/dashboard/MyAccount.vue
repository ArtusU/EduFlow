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
import axios from 'axios';
export default {
  methods: {
    async logout() {
      console.log('logout');
      function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
      }

      const csrfToken = getCookie('csrftoken');

      await axios
        .post('token/logout/', null, {
          headers: {
            'X-CSRFToken': csrfToken
          }
        })
        .then(response => {
          console.log('Logged out');
        })
        .catch(error => {
          console.log(error);
        });

      axios.defaults.headers.common['Authorization'] = '';
      localStorage.removeItem('token');
      this.$store.commit('removeToken');
      this.$router.push('/');
    }
  }
}
</script>