# Testing

## Validator Testing

### HTML Testing
https://validator.w3.org/ -
![html]()

### CSS Testing 
https://jigsaw.w3.org/css-validator/ - 
![css]()

### JS Testing
https://jshint.com/ - 

### Python
http://pep8online.com/ - I checked the app.py file using PEP8 online
![PEP8]()

### Accessibility test
https://wave.webaim.org - 
![wave valid]()




## Testing User Stories


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

## During Development I Fixed The Following Bugs

- When a user added the ingredients to the recipes they've appeared on the same line instead of seperate lines which made it difficult to read. The same was for instructions.
<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue1.png" width="300" height="300"/>
<br>

    - I wanted the user to be able to add ingredients and instructions so they all would appear on seperate lines in a list. At first I had the `input` field from Materialize then I changed it to `textarea` and added the class of .materialize-textarea so that when a user added an ingredient or a new step in the instructions they could just press enter to make a line break. I've also added a .helper-text to clearify for the user what to do.


    - I've also added a for loop with list element so the ingredients/instructions could iterate through.
Previous: `{{ recipe.category_name }}`.
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
    - I added `.splitlines()` = `{% for ingredient in recipe.ingredients.splitlines() %}` and that fixed the issue.

- The different steps for the instructions all have nr 1.
<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue3.png" width="300" height="300"/>
<br>

    - moved for loop inside list item
    
    -  <div>
                <ol>
                    {% for steps in recipe.instructions.splitlines() %}
                    <li>{{ steps }}</li>
                    {% endfor %}
                </ol>
            </div>

instead of:
{% for steps in recipe.instructions.splitlines() %}
            <div>
                <ol>
                    <li>{{ steps }}</li>
                </ol>
            </div>
            {% endfor %}

- I've had some responsiveness issues with the search bar. On smaller devices the input field was very small and buttons overlapping.
    - I've had added the Materialize class name "valign-wrapper" because I wanted it to be vertically aligned. I removed this and kept the center-align class and the buttons now appeared below the search bar on smaller devices making it much easier to fill out and search.

- Font weight for the logo "Yum Yum" was too big for iphone 5/SE making it appear on two lines. Even on Galaxy fold the logo jumped down a line.
    - I've added the class .hide-on-small-only from Materialize which hides the logo on small screens. This actually made it look much cleaner and not so cluttered in the navbar.

## Validator Testing

#### HTML Testing
https://validator.w3.org/ -
![html]()

#### CSS Testing 
https://jigsaw.w3.org/css-validator/ - 
![css]()

#### JS Testing
https://jshint.com/ - 

#### Python
http://pep8online.com/ - I checked the app.py file using PEP8 online
![PEP8]()

#### Accessibility test
https://wave.webaim.org - 
![wave valid]()

## Lighthouse Testing

I've ran the raport in Lighthouse when I considered myself almost done with the page and it had quite a good score, there was just some minor issues that needed to be fixed.
    - Add alt text to images
    - Add `rel="noopener"` to social media links
    - Add meta description to base.html

## I Manually Tested The Following Features
- Links in navbar works and takes you to the correct pages.
- Buttons on landing page takes you to the recipe page.
- Hover effect on links in navbar.
- All links works and opens in a new tab window.
- Links to social media platforms works and opens in a new tab window.

**Responsiveness**
I manually tested the responsiveness on all available devices in DevTools. Galaxy fold didn't display well, this is something I will have to fix in the future.

![galaxy fold](https://github.com/flisanp/ms2-barcelona-guide/blob/d4a033c7e48d4b2828d4fb14bf498dfe54db6248/readme%20assets/bugs/galaxy-fold.png)

## Testing User Stories 
 
1. As a user I easily want to find good and healthy recipes that I can make for my baby
2. As a user I want to be able to search for a specific ingredient in the recipes
3. As a user I want to be able to look for recipes sorted by category
4. As a user I want to be able to create my own account
5. As a user I want to upload my own recipes
6. As a user I want to be able to edit my recipes
7. As a user I want to be able to delete my recipes
8. As a user I want to be able to log in to my account
9. As a user I want to be able to log out of my account
10. As a site admin I want to be able to add new categories to the site
11. As a site admin I want to be able to edit categories
12. As a site admin I want to be able to delete categories

