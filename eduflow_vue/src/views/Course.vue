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
                            <li
                                v-for="lesson in lessons"
                                v-bind:key="lesson.id"
                            >
                                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
                            </li>
                            
                        </ul>
                    </div>
                    <div class="column is-10">
                        <template v-if="$store.state.user.isAuthenticated">
                            <template v-if="activeLesson">
                                <h2>{{ activeLesson.title }}</h2>
                                <p>{{ activeLesson.long_description }}</p>
                                <form v-on:submit.prevent="submitComment()">
                                    <div class="field">
                                        <label class="label">Name</label>
                                        <div class="control">
                                            <input type="text" class="input" v-model="comment.name">
                                        </div>
                                    </div>

                                    <div class="field">
                                        <label class="label">Content</label>
                                        <div class="control">
                                            <textarea class="textarea" v-model="comment.content"></textarea>
                                        </div>
                                    </div>

                                    <div 
                                        class="notification is-danger"
                                        v-for="error in errors"
                                        v-bind:key="error"
                                    >
                                        {{ error }}
                                    </div>

                                    <div class="field">
                                        <div class="control">
                                            <button class="button is-link">Submit</button>
                                        </div>
                                    </div>
                                </form>
                            </template>
                            <template v-else>
                                {{ course.long_description }}
                            </template>
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
            course: {},
            lessons: [],
            comment: {
                name: '',
                content: ''
            },
            activeLesson: null,
        }
    },
    mounted() {
        console.log('mounted')

        document.title = 'Courses | EduFlow'

        const slug = this.$route.params.slug

        axios
            .get(`/courses/${slug}/`)
            .then(response => {
                // console.log(response.data)

                this.course = response.data.course
                this.lessons = response.data.lessons

            })
        
    },
    methods: {
        setActiveLesson(lesson) {
            this.activeLesson = lesson
        },
        submitComment() {
            console.log('comment submited')

            axios
                .post(`/courses/${this.course.slug}/${this.activeLesson.slug}/`, this.comment)
                .then(response => {
                    this.comment.name = ''
                    this.comment.content = ''
                    alert('comment submitted')
                })
                .catch(error => {
                    console.log(error)
                })

        }
    }

}
</script>
