# Baby Food Recipes

[A live version of the page can be viewed here]()

![mockup image]()


This website is a recipe site for baby food. Users can search trough existing recipes and create an account where they can upload their own recipes and share them with other users.


# UX

#### The Goals For This Website Is To: 
- Provide a place where people can find good and healthy recipes for babies
- Share baby food recipes with other people
- Have a place to store own recipes
- Make it easy for users to navigate on the site to find what they are looking for


#### User Stories

1. As a user I easily want to find good and healthy recipes that I can make for my baby
![wireframe]()
2. As a user I want to be able to search for a specific ingredient in the recipes
![wireframe]()
3. As a user I want to be able to create an account where I can upload my own recipes
![wireframe]()
4. As a user I want to be able to edit my recipes
![wireframe]()
5. As a user I want to be able to delete my recipes
![wireframe]()
6. As a user I want to be able to log in and out of my account
![wireframe]()
7. 
![wireframe]()
8. 
![wireframe]()
9. 
![wireframe]()
10. 
![wireframe]()

#### Design 

![color palette]()


# Features

**Navbar** - Each page features a responsive Materialize navbar that’s collapsed to a burger icon when viewing on smaller screens. The navbar has a hover effect so when the user hovers over the different pages the text changes color. The navbar has links to the landing page *HOME*, recipes page *RECIPES*, registration page *SIGN UP* and login page *LOG IN*. When you are logged in the navbar has a link to your profile page *ACCOUNT* and when Admin is logged in there is also a link to a page for managing the categories *MANAGE CATEGORIES*.

**Home** - 

**Recipes** - 

**Footer** - Exists on the bottom of every page. Located in the center of the footer are four icons with links to the sites social media platforms. 

#### Features Left To Implement


# Technologies Used

- HTML5, CSS3, Javascript and Python3
- [GitPod](https://www.gitpod.io) - The developer used GitPod for their IDE while building the website.
- [GitHub](https://github.com) - This project uses GitHub to store the projects code after being pushed from Git.
- [Materialize](https://materializecss.com/) - This project uses Bootstrap to make the site responsive and to implement features such as the navbar and the buttons.
- [FontAwesome](https://fontawesome.com) - This project uses FontAwesome for social media icons.
- [Google Fonts](https://fonts.google.com) - This project uses Montserrat and Lora from Google Fonts.
- [Balsamiq](https://balsamiq.com) - The developer used Balsamiq to create wireframes.
- [DevTools](https://developers.google.com/web/tools/chrome-devtools) - The developer has used DevTools to test responsiveness and diagnose problems. The tool **Lighthouse** has been used to improve the website's quality. 
- [Tinypng](https://tinypng.com) - The developer used Tinypng for compressing images.
- [Freeformatter](https://www.freeformatter.com/) - The developer used Freeformatter for beautifying the code.
- [A11y](https://color.a11y.com) - The developer used A11y for checking the websites color contrast accessibility.
- [Wave](https://wave.webaim.org) - The developer used Wave for checking the websites color contrast accessibility. 
- [ResizeImage](https://resizeimage.net) - The developer used ResizeImage to resize images.
- [Coolors](https://coolors.co) - The developer used Coolors to create color palette.
- [Techsini](https://techsini.com/multi-mockup/index.php) - The developer used Techsini for creating the mockup image in the beginning of this README file.
- [Canva](https://www.canva.com) The developer used Canva for creating the favicon.



# Testing

#### I Manually Tested The Following Features
- Links in navbar works and takes you to the correct pages.
- Buttons on landing page 
- Hover effect on links in navbar.
- Links to social media platforms works and opens in a new tab window.

**Responsiveness**


#### Testing User Stories 


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

- The different steps for the instructions all have nr 1 



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

# Deployment
To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:
1. Navigate to flisanp repositories.
2. Select the one that is called ms2-barcelona-guide from the list.
3. Click on settings in the menu that is located to the top right.
4. Scroll down to "GitHub Pages"
5. Under "Source", Select Master Branch from the drop-down menu.
6. Click Save and the website is now deployed.

### How To Run The Code Locally
1. Log inte Gitpod with your account.
2. Navigate to the [repository](https://github.com/flisanp/ms3-baby-food-recipes).
3. Click the green GitPod button on the top right.
4. A new workspace will be created.

# Credits

#### Content



**Code**



#### Media

Apple and blueberry puree: https://unsplash.com/photos/QvMen4ChnoI
Fruit and veggie smoothie: https://unsplash.com/photos/wjt2-Vo7GA8
Pancakes: https://unsplash.com/photos/tKKe3aDvncE
Porridge: https://unsplash.com/photos/-eLS9k_uhUc
risotto: https://unsplash.com/photos/qIPRTMulc-g
Pumpkin soup: https://cdn.pixabay.com/photo/2018/03/20/09/18/plate-3242587_1280.jpg
chickpea rice: https://unsplash.com/photos/vCNLO20cuwY
mango chia: https://unsplash.com/photos/5fj-ShvSEnc
soppa: https://unsplash.com/photos/BA6FzJZ9IfY
soppa: https://unsplash.com/photos/BA6FzJZ9IfY

Recipes from:
https://www.eatingbirdfood.com/oatmeal-for-babies/
https://www.homemade-baby-food-recipes.com/
https://www.mylittlemoppet.com/easy-pumpkin-soup-recipe-babies/
https://plantbasedjuniors.com/
https://babyfoode.com/

  

#### Acknowledgements



<a target="_blank" href="https://icons8.com/icon/5Rd0v9hlYljM/baby-food">Baby Food</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
