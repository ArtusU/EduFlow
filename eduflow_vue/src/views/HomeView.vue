<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to EduFlow</h1>
        <h2 class="subtitle">EduFlow is a Learning Management System (LMS) that delivers a dynamic and immersive learning experience.</h2>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>
              <p>Manage your own study time</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study with others</h2>
              <p>Collaborate and exchange ideas and skills</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study from home</h2>
              <p>Manage your own study time</p>
            </div>
          </div>
          <div class="column is-12 has-text-centered">
            <a href="/sign-up" class="button is-info is-size-3 mt-6 mb-6">Click to get started</a>
          </div>
          <hr>
          <div 
              class="column is-3"
              v-for="course in courses"
              v-bind:key="course.id"
          >
              <CourseItem :course="course" />
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script>
import CourseItem from '@/components/CourseItem.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
      return {
          courses: []
      }
  },
  components: {
      CourseItem
  },
  mounted() {
      console.log('mounted')

      document.title = 'Welcome | EduFlow'

      axios
          .get('courses/get_frontpage_courses/')
          .then(response => {
              console.log(response.data)

              this.courses = response.data
          })
  }
}
</script>
