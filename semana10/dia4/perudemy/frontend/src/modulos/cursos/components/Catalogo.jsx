import React from 'react';

const Catalogo = () => {
    return (
        <div className="uk-container">
            <div className="flex gap-12">
                <div className="w-1/5 space-y-4 uk-visible@m">
                    <div>
                        <h4> Categories </h4>
                        <select className="selectpicker default" data-selected-text-format="count" data-size="7"
                            title="All Categories">
                            <option> Web Development </option>
                            <option> Mobile App </option>
                        </select>
                    </div>
                    <div>
                        <h4> Skill Levels</h4>
                        <div>
                            <div className="radio">
                                <input id="radio-1" name="radio" type="radio" checked/>
                                <label for="radio-1"><span className="radio-label"></span> Beginner <span> (25) </span>
                                </label>
                            </div>
                            <br/>
                            <div className="radio">
                                <input id="radio-2" name="radio" type="radio"/>
                                <label for="radio-2"><span className="radio-label"></span> Entermidate <span> (25) </span>
                                </label>
                            </div>
                        </div>
                    </div>
                    <div>
                        <h4> Course rating </h4>

                        <form>
                            <div className="radio">
                                <input id="course-rate-1" name="radio" type="radio" checked/>
                                <label for="course-rate-1"><span className="radio-label"></span>

                                    <div className="star-rating leading-4">
                                        <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                        <span className="star"></span> <span className="star"></span>
                                    </div> (320)

                                </label>
                            </div>
                            <br/>
                            <div className="radio">
                                <input id="course-rate-2" name="radio" type="radio"/>
                                <label for="course-rate-2"><span className="radio-label"></span>

                                    <div className="star-rating leading-4">
                                        <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                        <span className="star"></span> <span className="star half"></span>
                                    </div> (160)

                                </label>
                            </div>
                        </form>

                    </div>

                    <div>
                        <h4> Course type </h4>
                        <form>
                            <div className="radio">
                                <input id="course-type-1" name="radio" type="radio" checked/>
                                <label for="course-type-1"><span className="radio-label"></span>Free (42) </label>
                            </div>
                            <br/>
                            <div className="radio">
                                <input id="course-type-2" name="radio" type="radio"/>
                                <label for="course-type-2"><span className="radio-label"></span> Paid (42)</label>
                            </div>
                        </form>
                    </div>

                    <div>
                        <h4> Duration </h4>
                        <form>
                            <div className="radio">
                                <input id="course-duration-1" name="radio" type="radio" checked/>
                                <label for="course-duration-1"><span className="radio-label"></span> +5 Hourse (23) </label>
                            </div>
                            <br/>
                        </form>
                    </div>

                </div>
                <div className="lg:w-4/5">

                    <div className="md:flex justify-between items-center mb-5">
                        <div>
                            <h2> Web Development Courses </h2>
                            <p className=" uk-visible@m"> choose from +10.000 courses with new
                                additions published every months </p>
                        </div>
                        <div className="flex">

                            <div
                                className="bg-white border border-gray-300 divide-gray-300 divide-x flex mr-3 rounded-md align-self-center">
                                <a href="courses.html" className="px-4 py-2 text-lg text-gray-600"
                                    data-tippy-placement="top" title="Course list">
                                    <i className="icon-feather-grid"></i></a>
                                <a href="courses-list.html" className="px-4 py-2 text-lg text-gray-400"
                                    data-tippy-placement="top" title="Course Grid">
                                    <i className="icon-feather-list"></i></a>
                            </div>
                            <div className="w-40">
                                <select className="selectpicker ml-3" data-size="7">
                                    <option value=""> Newest </option>
                                    <option value="1">Popular</option>
                                    <option value="2">Free</option>
                                    <option value="3">Premium</option>
                                </select>
                            </div>

                        </div>
                    </div>

                    <div className="grid md:grid-cols-3 sm:grid-cols-2 gap-4">
                        <a href="course-intro.html" className="course-card">
                            
                            <div className="course-card-thumbnail">
                                <div className="course-card-thumbnail-inner">
                                    <img src="assets/images/course/img-2.jpg" alt=""/>
                                </div>
                                <span className="play-btn-trigger"></span>
                            </div>
                            <div className="course-card-content">
                                <h3>Learn Angular Fundamentals From beginning to advance</h3>
                                <span className="instructor"> Stella Johnson </span>
                                <ul className="course-info">
                                    <li> 13 total hours </li>
                                    <span className="middot">·</span>
                                    <li> 151 lectures </li>
                                </ul>
                            </div>
                            <div className="course-card-foot">
                                <div className="star-rating leading-4">
                                    <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                    <span className="star"></span>
                                    <span className="star half"></span>
                                </div>
                                <span className="pricing">
                                    $14.99
                                </span>
                            </div>
                        </a>
                        <a href="course-intro.html" className="course-card">
                            <div className="course-card-thumbnail">
                                <div className="course-card-thumbnail-inner">
                                    <img src="assets/images/course/img-1.jpg" alt=""/>
                                </div>
                                <span className="play-btn-trigger"></span>
                            </div>
                            <div className="course-card-content">
                                <h3>Bootstrap 4 From Scratch to Expert With 5 Real Projects</h3>
                                <span className="instructor"> Stella Johnson </span>
                                <ul className="course-info">
                                    <li> 13 total hours </li>
                                    <span className="middot">·</span>
                                    <li> 151 lectures </li>
                                </ul>
                            </div>
                            <div className="course-card-foot">
                                <div className="star-rating leading-4">
                                    <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                    <span className="star"></span>
                                    <span className="star half"></span>
                                </div>
                                <span className="pricing">
                                    $12.99
                                </span>
                            </div>
                        </a>
                        <a href="course-intro.html" className="course-card">
                            <div className="course-card-thumbnail">
                                <div className="course-card-thumbnail-inner">
                                    <img src="assets/images/course/img-7.jpg" alt=""/>
                                </div>
                                <span className="play-btn-trigger"></span>
                            </div>
                            <div className="course-card-content">
                                <h3>Learn Modern Web Designer And Developer Course</h3>
                                <span className="instructor"> Stella Johnson </span>
                                <ul className="course-info">
                                    <li> 13 total hours </li>
                                    <span className="middot">·</span>
                                    <li> 151 lectures </li>
                                </ul>
                            </div>
                            <div className="course-card-foot">
                                <div className="star-rating leading-4">
                                    <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                    <span className="star"></span>
                                    <span className="star half"></span>
                                </div>
                                <span className="pricing">
                                    $16.99
                                </span>
                            </div>
                        </a>
                        <a href="course-intro.html" className="course-card">
                            <div className="course-card-thumbnail">
                                <div className="course-card-thumbnail-inner">
                                    <img src="assets/images/course/img-3.jpg" alt=""/>
                                </div>
                                <span className="play-btn-trigger"></span>
                            </div>
                            <div className="course-card-content">
                                <h3>The Complete JavaScript From beginning to advance</h3>
                                <span className="instructor"> Stella Johnson </span>
                                <ul className="course-info">
                                    <li> 13 total hours </li>
                                    <span className="middot">·</span>
                                    <li> 151 lectures </li>
                                </ul>
                            </div>
                            <div className="course-card-foot">
                                <div className="star-rating leading-4">
                                    <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                    <span className="star"></span>
                                    <span className="star half"></span>
                                </div>
                                <span className="pricing">
                                    $12.99
                                </span>
                            </div>
                        </a>
                        <a href="course-intro.html" className="course-card">       
                            <div className="course-card-thumbnail">
                                <div className="course-card-thumbnail-inner">
                                    <img src="assets/images/course/img-4.jpg" alt=""/>
                                </div>
                                <span className="play-btn-trigger"></span>
                            </div>
                            <div className="course-card-content">
                                <h3> Become a Web Developer from Scratch to Advanced</h3>
                                <span className="instructor"> Stella Johnson </span>
                                <ul className="course-info">
                                    <li> 13 total hours </li>
                                    <span className="middot">·</span>
                                    <li> 151 lectures </li>
                                </ul>
                            </div>
                            <div className="course-card-foot">
                                <div className="star-rating leading-4">
                                    <span className="star"></span> <span className="star"></span> <span className="star"></span>
                                    <span className="star"></span>
                                    <span className="star half"></span>
                                </div>
                                <span className="pricing">
                                    $11.99
                                </span>
                            </div>
                        </a>
                    </div>
                    <ul className="uk-pagination uk-flex-center uk-margin-medium">
                        <li className="uk-active">
                            <span>1</span>
                        </li>
                        <li>
                            <a href="#">2</a>
                        </li>
                        <li>
                            <a href="#">3</a>
                        </li>
                        <li>
                            <a href="#">4</a>
                        </li>
                        <li>
                            <a href="#">5</a>
                        </li>
                        <li>
                            <a href="#"><i className="icon-feather-chevron-right uk-margin-small-top"></i></a>
                        </li>
                        <li>
                            <a href="#">12</a>
                        </li>
                    </ul>

                </div>
            </div>
        </div>
    )
}

export default Catalogo;