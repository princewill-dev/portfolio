<x-layout>

    <div class="rn-slider-area" style="padding-bottom: 20px !important">
        <div class="slide slider-style-1 with-square-box" style="padding-bottom: 20px !important">
            <div class="container">
                <div class="row row--30 align-items-center">

                    <div class="col-md-12">
                        <div class="content">
                            
                            <div class="inner">
                                <img src="images/user_icon.jpg" alt="Personal Portfolio Images" width="100px" style="border: 2px solid #fff; border-radius: 5px;">
                                <br>
                                <br>
                                <span>Hi, my name is Princewill</span>
                                <h1 class="title">I build solutions for the web.</span></h1>
                                <div>
                                    
                                    <p class="description"> I'm a web developer based in Lagos, Nigeria. I craft websites and digital services that prioritizes the user's experience by removing ununnecessary bottlenecks and frictions.</p>

                                    <!--<a class="rn-btn" target="_blank" href="mailto:hello@princewilldev.com"><span>Let's talk</span></a>-->
                                    
                                    <h3 style="font-size: 30px;">Get in touch</h3>
                                    <a href="mailto:hello@princewilldev.com">hello@princewilldev.com</a>
                                    <br>
                                    <br>
                                    <a class="rn-btn" href="/Resume-Chibuike-Princewill-Ezekude.pdf" target="_blank">My Resume</a>
                                    
                                    <div class="social-share-inner-left">
                                        <br>
                                        <ul class="social-share d-flex liststyle">
                                            <li class="twitter"><a href="https://twitter.com/princewill_dev"><i data-feather="twitter" target="_blank"></i></a></li>
                                            <li class="linkedin"><a href="https://www.linkedin.com/in/princewilldev" target="_blank"><i data-feather="linkedin"></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <div class="container" style="padding: 20px;">
        <div class="row">
            <div class="rn-skill-area section-height">
                <div class="inner slide">
                    <h5 class="title">
                        My Skills
                    </h5>
                    <div class="skill-share-inner pt--50">
                        <span class="title">Primary Skills on</span>
                        <ul class="skill-share d-flex liststyle">
                            
                            <li><img src="assets/images/icons/icons-18.png" alt="Icons Images"></li>
                            <li><img src="assets/images/icons/css-icon.png" alt="Icons Images"></li>
                            <li><img src="assets/images/icons/javascript.png" alt="Icons Images"></li>
                            <li><img src="assets/images/icons/bootstrap.png" alt="Icons Images"></li>
                            <li><img src="assets/images/icons/github.png" alt="Icons Images"></li>
                            <li><img src="assets/images/icons/php.png" alt="Icons Images"></li>
                            <li><img src="assets/images/icons/laravel.jpeg" alt="Icons Images"></li>
                            
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="rn-portfolio-area rn-section-gap section-separator" id="portfolio">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="section-title text-center">
                        {{-- <span class="subtitle">Visit my portfolio and keep your feedback</span> --}}
                        <h2 class="title">My Projects</h2>
                    </div>
                </div>
            </div>

            <div class="row row--25 mt--10 mt_md--10 mt_sm--10">

                <div data-aos="fade-up" data-aos-delay="100" data-aos-once="true" class="col-lg-6 col-xl-4 col-md-6 col-12 mt--50 mt_md--30 mt_sm--30">
                    <div class="rn-portfolio" data-bs-toggle="modal" data-bs-target="#exampleModalCenter">
                        <div class="inner">
                            <div class="thumbnail">
                                <a href="javascript:void(0)">
                                    <img src="images/notes-home.png" alt="Personal Portfolio Images">
                                </a>
                            </div>
                            <div class="content">
                                <div class="category-info">
                                    <div class="category-list">
                                        <a href="javascript:void(0)">Notes</a>
                                    </div>
                                    {{-- <div class="meta">
                                        <span><a href="javascript:void(0)"><i class="feather-heart"></i></a> 600</span>
                                    </div> --}}
                                </div>
                                <p>This is a note taking web app that that allows you to priavtely save and retrieve notes anonymously with a 4 digit code. </p>
                                <a href="https://notes.princewilldev.com/" target="_blank">view project<i class="feather-arrow-up-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div data-aos="fade-up" data-aos-delay="300" data-aos-once="true" class="col-lg-6 col-xl-4 col-md-6 col-12 mt--50 mt_md--30 mt_sm--30">
                    <div class="rn-portfolio" data-bs-toggle="modal" data-bs-target="#exampleModalCenter">
                        <div class="inner">
                            <div class="thumbnail">
                                <a href="javascript:void(0)">
                                    <img src="images/task-home.png" alt="Personal Portfolio Images">
                                </a>
                            </div>
                            <div class="content">
                                <div class="category-info">
                                    <div class="category-list">
                                        <a href="javascript:void(0)">Tasker</a>
                                    </div>
                                </div>
                                <p>A multi-purpose web platform that allows to organize personal notes, shorten URLs, save and share files easily. </p>
                                <a href="https://task.princewilldev.com/" target="_blank">view project<i class="feather-arrow-up-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

</x-layout>