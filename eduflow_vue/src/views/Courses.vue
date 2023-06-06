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
                            <CourseItem :course="course" />

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
import CourseItem from '@/components/CourseItem.vue'
import axios from 'axios'

export default {
    data() {
        return {
            courses: [],
        }
    },
    components: {
        CourseItem
    },
    mounted() {

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

