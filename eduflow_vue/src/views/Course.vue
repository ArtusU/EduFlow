<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{ course.title }}</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Table of contents</h2>
                        <ul>
                            <li>Introduction</li>
                            <li>Introduction</li>
                            <li>Introduction</li>
                            <li>Introduction</li>
                        </ul>
                    </div>
                    <div class="column is-10">
                        <template v-if="$store.state.user.isAuthenticated">
                            <h2>Active Lesson title</h2>
                            <p>{{ course.long_description }}</p>
                        </template>
                        <template v-else>
                            <h2>Restricted access</h2>
                            
                            <p>You need to have an account to continue!</p>
                        </template>
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
            course: [],
        }
    },
    mounted() {
        console.log('mounted')

        document.title = 'Courses | EduFlow'

        const slug = this.$route.params.slug

        axios
            .get(`/courses/${slug}/`)
            .then(response => {
                console.log(response.data)

                this.course = response.data

            })
        
    },

}
</script>
