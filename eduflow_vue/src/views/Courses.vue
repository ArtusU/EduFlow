<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Courses</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-2">
                        <aside class="menu">
                            <p class="menu-label">Categories</p>
                            <ul class="menu-list">
                                <li><a href="">All Courses</a></li>
                                <li><a href="">Programing</a></li>
                                <li><a href="">Design</a></li>
                                <li><a href="">UX</a></li>
                            </ul>
                        </aside>
                    </div>
                    <div class="column is-10">
                        <div class="columns is-multiline">
                            <div 
                                class="column is-4"
                                v-for="course in courses"
                                v-bind:key="course.id"
                            >
                            <div class="card">
                                <div class="card-image">
                                    <figure class="image is-4by3">
                                    <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                                    </figure>
                                </div>

                                <div class="card-content">
                                    <div class="media">
                                    <!-- <div class="media-left">
                                        <figure class="image is-48x48">
                                        <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
                                        </figure>
                                    </div> -->
                                    <div class="media-content">
                                        <p class="title is-4">{{ course.title }}</p>
                                    </div>
                                    </div>
                                    <div class="content">
                                        {{ course.short_description }}
                                        <br>
                                        <router-link :to="{name: 'Course', params: {slug: course.slug}}">More</router-link>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div class="column is-12">
                            <nav class="pagination">
                                <a class="pagination-previous">Previous</a>
                                <a class="pagination-next">Next</a>
                            </nav>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        </section>
    </div>
</template>




<script>
import axios from 'axios'

export default {
    data() {
        return {
            courses: [],
        }
    },
    mounted() {
        console.log('mounted')

        document.title = 'Courses | EduFlow'

        axios
            .get('/courses/')
            .then(response => {
                console.log(response.data)

                this.courses = response.data

            })
        
    },

}
</script>

