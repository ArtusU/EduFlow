<template>
    <div class="about">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Create course</h1>
            </div>
        </div>

        <section class="section">
            <div class="mb-6 px-6 py-4 has-background-grey-lighter">
                <h2 class="subtitle">Meta information</h2>

                <div class="field">
                    <label>Title</label>
                    <input type="text" class="input">
                </div>

                <div class="field">
                    <label>Short description</label>
                    <textarea class="textarea"></textarea>
                </div>

                <div class="field">
                    <label>Long description</label>
                    <textarea class="textarea"></textarea>
                </div>

                <div class="field">
                    <div class="select is-multiple">
                        <select multiple size="10">
                            <option>
                                Option 1
                            </option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="mb-6 px-6 py-4 has-background-grey-lighter">
                <h2 class="subtitle">Lessons</h2>

                <div class="mb-4">
                    <h3 class="subtitle is-size-6">Lesson</h3>

                    <div class="field">
                        <label>Title</label>
                        <input 
                            type="text" 
                            class="input" 
                        >
                    </div>

                    <div class="field">
                        <label>Short description</label>
                        <textarea class="textarea"></textarea>
                    </div>

                    <div class="field">
                        <label>Long description</label>
                        <textarea class="textarea"></textarea>
                    </div>

                    <hr>
                </div>

                <button class="button is-primary">Add lesson</button>
            </div>

            <div class="field buttons">
                <button class="button is-success">Save as draft</button>
                <button class="button is-info">Submit for review</button>
            </div>
        </section>
    </div>
</template>
