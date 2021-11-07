# Testing



### Testing User Stories


1. As a user I easily want to find good and healthy recipes that I can make for my baby
![wireframe]()
2. As a user I want to be able to search for a specific ingredient in the recipes
![wireframe]()
3. As a user I want to be able to look for recipes sorted by category
![wireframe]()
4. As a user I want to be able to create my own account
![wireframe]()
5. As a user I want to upload my own recipes
![wireframe]()
6. As a user I want to be able to edit my recipes
![wireframe]()
7. As a user I want to be able to delete my recipes
![wireframe]()
8. As a user I want to be able to log in to my account
![wireframe]()
9. As a user I want to be able to log out of my account
![wireframe]()
10. As a site admin I want to be able to add new categories to the site
![wireframe]()
11. As a site admin I want to be able to edit categories
![wireframe]()
12. As a site admin I want to be able to delete categories
![wireframe]()

### During Development I Fixed The Following Bugs

- When a user added the ingredients to the recipes they've appeared on the same line instead of seperate lines which made it difficult to read. The same was for instructions.
<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue1.png" width="300" height="300"/>
<br>

    - I wanted the user to be able to add ingredients and instructions so they all would appear on seperate lines in a list. At first I had the `input` field from Materialize then I changed it to `textarea` and added the class of .materialize-textarea so that when a user added an ingredient or a new step in the instructions they could just press enter to make a line break. I've also added a .helper-text to clearify for the user what to do.


    - I've also added a for loop with list element so the ingredients/instructions could iterate through.
Previous: `{{ recipe.category_name }}`
Changed it to:
    `{% for ingredient in recipe.ingredients %}`
            `<div>`
                `<ul>`
                    `<li>`
                        `{{ ingredient }}`
                    `</li>`
                `</ul>`
            `</div>`
    `{% endfor %}`

- This solved the issue but now all the letters was on a new line.
<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue2.png" width="300" height="300"/>
<br>
    - I added .splitlines() and that the fixed problem.

- The different steps for the instructions all have nr 1.
!<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue3.png" width="300" height="300"/>
<br>

#### HTML Testing
https://validator.w3.org/ -
![html]()


#### CSS Testing 
https://jigsaw.w3.org/css-validator/ - 
![css]()


#### JS Testing
https://jshint.com/ - 


#### Accessibility test
https://wave.webaim.org - 
![wave valid]()

#### I Manually Tested The Following Features
- Links in navbar works and takes you to the correct pages.
- Buttons on landing page takes you to the map and shows the right markers.
- Info window opens when markers being clicked.
- Previous info window close when clicking on a new marker.
- Links in info window works and open the correct page in a new window.
- Hover effect on links in navbar.
- All links works and opens in a new tab window.
- Scroll to top button appears on scroll and takes you to the top of the page.
- Toggle sharing button works and shares the site accordingly.
- Links to social media platforms works and opens in a new tab window.

**Responsiveness**
I manually tested the responsiveness on all available devices in DevTools. Galaxy fold didn't display well, this is something I will have to fix in the future.

![galaxy fold](https://github.com/flisanp/ms2-barcelona-guide/blob/d4a033c7e48d4b2828d4fb14bf498dfe54db6248/readme%20assets/bugs/galaxy-fold.png)

#### Testing User Stories 

1. As a first time visitor to Barcelona I would like to see where the best tourist attractions are located. ![user story 1](https://github.com/flisanp/ms2-barcelona-guide/blob/e4eda1e7e7460d614dd317749dc9e6cfceb02e17/readme%20assets/user%20stories/discover.png) ![map](https://github.com/flisanp/ms2-barcelona-guide/blob/bd065637704be796aedd247864589655ba39dda9/readme%20assets/user%20stories/discover-map.png)
    - On the landing page is a call to action button that says "DISCOVER" which leads you to the map that shows markers for the  different locations. The user can click on each marker which opens a info window where the user can find the main information and be directed to a website for further reading.
2. As a traveller who is planning to visit Barcelona I would like to find a good hotel for my visit. ![user story 2](https://github.com/flisanp/ms2-barcelona-guide/blob/e4eda1e7e7460d614dd317749dc9e6cfceb02e17/readme%20assets/user%20stories/sleep.png) ![map](https://github.com/flisanp/ms2-barcelona-guide/blob/bd065637704be796aedd247864589655ba39dda9/readme%20assets/user%20stories/sleep-map.png)
    - On the landing page is a call to action button that says "SLEEP" which leads you to the map that shows markers for different hotels. The user can click on each marker which opens a info window where the user can find the main information and be directed to a website for further reading.
3. As a traveller visiting Barcelona I would like to see a map over the city to find out if there’s any restaurants located close to my hotel. ![user story 3](https://github.com/flisanp/ms2-barcelona-guide/blob/bd065637704be796aedd247864589655ba39dda9/readme%20assets/user%20stories/eat-map.png)
    - On the landing page is a call to action button that says "EAT" which leads you to the map that shows markers for different hotels. The user can click on each marker which opens a info window where the user can find the main information and be directed to a website for further reading.
4. As a traveller aiming to visit Barcelona I would like to see the weather forecast to better plan my packing for the trip. ![user story 4](https://github.com/flisanp/ms2-barcelona-guide/blob/bd065637704be796aedd247864589655ba39dda9/readme%20assets/user%20stories/weather-forecast.png)
    - In the navbar on the top right is a link that says WEATHER where the user can find a 7 day weather forecast.
5. As a traveller who is planning to visit Barcelona with friends I would like to have an easy way to share the site with tips that I've found to my travel companions. ![user story 4](https://github.com/flisanp/ms2-barcelona-guide/blob/bd065637704be796aedd247864589655ba39dda9/readme%20assets/user%20stories/toggle-sharing-folded.png) ![sharing](https://github.com/flisanp/ms2-barcelona-guide/blob/bd065637704be796aedd247864589655ba39dda9/readme%20assets/user%20stories/toggle-sharing-expand.png)
    - In the bottom left on every page is a toggle sharing button that will link the site through all of the most popular social media platforms. The user can also email the link or print it.


#### During Development I Fixed The Following Bugs


- I wanted the user to be able to add ingredients and instructions so they would appear on new lines. At first I had the <input> field from Materialize then I changed it to <textarea> and added the class of materialize-textarea so that when a user added an ingredient they could just press enter and next ingredient would appear on a new line.


- Ingredients and Instructions on the recipe card was showing without any linebreaks.
Previous:{{ recipe.category_name }}
Added a for loop with list element so the ingredients/instructions could iterate through:
    {% for ingredient in recipe.ingredients %}
            <div>
                <ul>
                    <li>
                        {{ ingredient }}
                    </li>
                </ul>
            </div>
    {% endfor %} 

- This solves the issue but now all the letters was on a new line.
I added .splitlines() and that problem was solved.

- The instructions all have nr 1 






- Issue with previous info window not closing when clicking on a new marker.
  ![issue markers](https://github.com/flisanp/ms2-barcelona-guide/blob/8a4491fa0c045600c8d1a4bcaa7f92e268c14af0/readme%20assets/bugs/issue-markers.png)

    - I found one error in consol declaring that `infoObj` was not defined.
    ![not defined error](https://github.com/flisanp/ms2-barcelona-guide/blob/120ca893eb8fd8569b3f8009ffa2d828cf9aba46/readme%20assets/bugs/not-defined-error.png) 
    
    - Defined `var infoObj= [];`
    ![not defined solution](https://github.com/flisanp/ms2-barcelona-guide/blob/120ca893eb8fd8569b3f8009ffa2d828cf9aba46/readme%20assets/bugs/not-defined-solution.png)
  

- Links in navbar was difficult to read because overlapping text on pages.
![menu links overlapping](https://github.com/flisanp/ms2-barcelona-guide/blob/5b2719de928c21d56b34213f628b4a3a61b8b030/readme%20assets/bugs/menu-links-overlapping.png)
   - Added the bootstrap class `bg-white` to the navbar.

- Menu overlapping text on the landing page when checking responsiveness on mobile
![menu overlapping](https://github.com/flisanp/ms2-barcelona-guide/blob/5b2719de928c21d56b34213f628b4a3a61b8b030/readme%20assets/bugs/menu-overlapping.png)
 - Added padding to the class `hero-text`

- I had some contrast issues with my design in the beginning. My image and text colors did not work well together.
![contrasting issues](https://github.com/flisanp/ms2-barcelona-guide/blob/8a4491fa0c045600c8d1a4bcaa7f92e268c14af0/readme%20assets/bugs/contrasting-issue.png)
![contrast issues white](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/contrast-issues-white.png)
    - I had to rethink my design and I changed both hero image and text color. I added an overlay on the the image and changed the text color to white and blue but I still got warnings in Wave telling me there were still low contrast between text and background. I found out that they are testing the text against the css background and not the image in case the image isn't loading.
    ![wave test](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/wave.png)
    - I changed the background color with css to a dark blue.

- Got warnings in Wave with contrast issues on my implemented weather forecast that had presets. 
![contrast weathermap](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/contrast-weathermap.png)
    - I had to override the presets by adding !important to css.

#### HTML Testing
https://validator.w3.org/ - No errors or warnings to show.
![html](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/html-valid.png)


#### CSS Testing 
https://jigsaw.w3.org/css-validator/ - showed 2 warnings regarding bootstrap presets.
![css](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/css-valid.png)


#### JS Testing
https://jshint.com/ - showed the following warnings:

![script](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/script-js.png)
![map](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/map-js.png)
![map](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/map-unused.png)

Warnings regarding *unused variable*: those functions are being called from the HTML file, so within the context of just the js file they are undefined, but they are in use by the HTML file. JShint only validates the JavaScript file and doesn't take into account that functions may be being called from outside the file.

Warning regarding *Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (closeOtherInfo, map, infoObj)*: I will not have the time to solve this semantic warning issue now without breaking  the code. The functionality of the code works despite this so I've decided to keep it like that for the time beeing and fix it in the future.

#### Accessibility test
https://wave.webaim.org - No warnings to show
![wave valid](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/bugs/wave-valid.png)