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
![user_story_1](static/images/README/user-stories/user-story-1.png)
2. As a user I want to be able to search for a specific ingredient in the recipes
![user_story_2](static/images/README/user-stories/user-story-2.png)
3. As a user I want to be able to look for recipes sorted by category
![user_story_3](static/images/README/user-stories/user-story-3.png)
4. As a user I want to be able to register my own account
![user_story_4](static/images/README/user-stories/user-story-4.png)
5. As a user I want to upload my own recipes
![user_story_5](static/images/README/user-stories/user-story-5.png)
6. As a user I want to be able to edit my recipes
![user_story_6](static/images/README/user-stories/user-story-6.png)
7. As a user I want to be able to delete my recipes
![user_story_7](static/images/README/user-stories/user-story-7.png)
8. As a user I want to be able to log in to my account
![user_story_8](static/images/README/user-stories/user-story-8.png)
9. As a user I want to be able to log out of my account
![user_story_9](static/images/README/user-stories/user-story-9.png)
10. As a site admin I want to be able to add new categories to the site
![user_story_10](static/images/README/user-stories/user-story-10.png)
11. As a site admin I want to be able to edit categories
![user_story_11](static/images/README/user-stories/user-story-11.png)
12. As a site admin I want to be able to delete categories
![user_story_12](static/images/README/user-stories/user-story-12.png)

## During Development I Fixed The Following Bugs

- When a user added the ingredients to the recipes they've appeared on the same line instead of seperate lines which made it difficult to read. The same was for instructions.  
![issue-1](static/images/README/bugs/issue1copy.png)
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
![issue-1](static/images/README/bugs/issue2copy.png)
<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue2.png" width="300" height="300"/>
<br>
    - I added `.splitlines()`  
     = `{% for ingredient in recipe.ingredients.splitlines() %}` and that fixed the issue.

- The different steps for the instructions all have nr 1.  
![issue-1](static/images/README/bugs/issue3copy.png)
<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/issue3.png" width="300" height="300"/>
<br>

    moved for loop inside list item:
    
      <div>
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


## Lighthouse Testing

I've ran the report in Lighthouse when I considered myself almost done with the page and it had quite a good score, there was just some minor issues that needed to be fixed.  
    - Add alt text to images  
    - Add `rel="noopener"` to social media links  
    - Add meta description to base.html  

## I Manually Tested The Following Features
- Home  
    - All links in navbar takes you to the correct pages
    - Button "Show recipes" takes you to the recipe page
    - All links to social media platforms in footer opens in a new tab window   
    - Hover effect on links in navbar
- Recipes
    - Search function finds the correct recipes
    - "Reset" button clears the search bar
    - Links to the different categories displays the correct recipes
- Sign Up
    - Input fields displays the text to the user and hides the password
    - User being added to the database upon registration and redirects to account page
    - Error message "Username already exists" displays if you try to type in an already existing username
    - Link "Log In" leads to Log In page
- Log In
    - Input fields displays the text to the user and hides the password
    - "Log In" button redirects to account page
    - Link "Register Now" leads to Sign Up page
- Account
    - Users own recipes appears on their account page
    - "Add recipe" button redirects to add recipe page
    - "Edit" button redirects to edit recipe page
    - "Delete" button opens confirmation modal
        - "Yes" on modal deletes the recipe from database
        - "No" on modal close the modal without any changes being made
- Log Out
    - User being logged out from Account and redirected to Log In page
- Add recipe
    - All fields in form are being filled out as expected
    - Submitting the form will not work without all fields being filled out
    - If filled out correcly recipe is being added to the database and diaplays on account page and recipe page
    - Ingredients are being displayed in a list if you press enter after every ingredient
    - Instructions are being displayed in a ordered list if you press enter efter every step
    - "Cancel" button takes you back to account page
- Edit recipe
    - Form is prefilled with the previous information
    - "Cancel" button takes you back to recipe page
    - "Update recipe" button updates recipe in database
- Manage Categories
    - Only visible when Admin is logged in
    - All tabs open and displays an "edit" and "delete" button
    - "Edit" button redirects to edit category page
    - "Add new category" button redirects to add category page
     - "Delete" button opens confirmation modal
        - "Yes" on modal deletes the category from database
        - "No" on modal close the modal without any changes being made
- Edit Category
    - The category name is prefilled in the input field
    - "Cancel" button takes you back to manage categories page
    - "Update category" button updates category in database
- Add Category
    - Submitting the form will not work without the field being filled out
    - "Cancel" button takes you back to manage categories page
    - Category is being added to database and displays on managae category page and as an option for users when they add a new recipe


**Responsiveness**  
To make sure that the site is responsive:
 - I manually tested it on all available devices in DevTools
 - I've used the site [Responsinator](http://www.responsinator.com/?url=baby-food.herokuapp.com%2Fhome)


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

