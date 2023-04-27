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
                        <asside class="menu">
                            <p class="menu-label">Categories</p>
                            <ul class="menu-list">
                                <li><a href="">All Courses</a></li>
                                <li><a href="">Programing</a></li>
                                <li><a href="">Design</a></li>
                                <li><a href="">UX</a></li>
                            </ul>
                        </asside>
                    </div>

                    <div class="column is-10">
                       <div class="colums is-multiline">
                        <div class="column is-4">
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
                                        <p class="title is-4">John Smith</p>
                                        <p class="subtitle is-6">@johnsmith</p>
                                    </div>
                                    </div>

                                    <div class="content">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                    Phasellus nec iaculis mauris. <a>@bulmaio</a>.
                                    <a href="#">#css</a> <a href="#">#responsive</a>
                                    <br>
                                    <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                                    </div>
                                </div>
                            </div>
                        </div>
                       </div>
                       <div class="column is-12">
                            <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                            <a class="pagination-previous">Previous</a>
                            <a class="pagination-next">Next page</a>
                            <ul class="pagination-list">
                                <li><a class="pagination-link" aria-label="Goto page 1">1</a></li>
                                <li><span class="pagination-ellipsis">&hellip;</span></li>
                                <li><a class="pagination-link" aria-label="Goto page 45">45</a></li>
                                <li><a class="pagination-link is-current" aria-label="Page 46" aria-current="page">46</a></li>
                                <li><a class="pagination-link" aria-label="Goto page 47">47</a></li>
                                <li><span class="pagination-ellipsis">&hellip;</span></li>
                                <li><a class="pagination-link" aria-label="Goto page 86">86</a></li>
                            </ul>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

