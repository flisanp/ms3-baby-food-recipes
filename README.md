# Yum Yum - Baby Food Recipes  

[A live version of the page can be viewed here](https://baby-food.herokuapp.com/home)  

![mockup image](static/images/README/mockup.png)  


Yum Yum is a recipe site for baby food. Users can search through existing recipes and create an account where they can upload and store their own recipes and share them with other users. As a new mom I've realized the importance of finding good and healthy recipes for my kid. I've also realized the importance of finding them fast due to lack of time. This is why I wanted to create this website for me and parents alike that could benefit from this service.  

---  

## UX  

### The Goals For This Website Is To:  

- Provide a place where people can easily find good and healthy recipes for babies
- Be able to create an account to store your own recipes
- Share baby food recipes with other people
- Make it easy for users to navigate the site on any device   

### User Stories  

-   As a user I easily want to find good and healthy recipes that I can make for my baby
-   As a user I want to be able to search for a specific ingredient in the recipes
-   As a user I want to be able to look for recipes sorted by category
-   As a user I want to be able to register my own account
-   As a user I want to be able to log in to my account
-   As a user I want to be able to log out of my account
-   As a user I want to upload my own recipes
-   As a user I want to be able to edit my recipes
-   As a user I want to be able to delete my recipes
-   As a site admin I want to be able to add new categories to the site
-   As a site admin I want to be able to edit categories
-   As a site admin I want to be able to delete categories  

### Design   

With a potential user in mind being a parent with restricted time searching for recipes they can make for their babies, I wanted to have a minimalistic design and focus on giving the user an easy and quick way of locate what they're looking for. That is why I choose to have the recipes on a card that immidiately shows the recipes when they click on them rather then sending the user to an additional page. This way they can click their way through several recipes to see if it's something that interest them without leaving the main page. 
![color palette](static/images/README/recipe-cards.png) 

#### Colors  

I didn't want to have the classic pastel color scheme that you normally see when it's connected to babies and that is why I choose to have a color palette with calm colors that feels a little bit more sophisticated and also has a good contrast ratio. The name Yum Yum is for me a playful way of saying that something is good when you're talking to a baby about food and also indicates that the website is designed with babies in mind. 

![color palette](static/images/README/color-palette.png)

#### Typography

The main fonts that I choose for this project is Montserrat and Lato which are two quite simple sans-serif fonts that gives a clean expression and are easy to read. For the name of the website I have used Gluten that with it's round shapes fits well with the kids theme. It's also being used for flash messages to tie the page together. This is a font that I think could feel a little overhelming and unserious if it's used too much so that is why I choose to use it sparingly.  

### Wireframes  

Wireframes can be viewed [here](static/images/README/wireframes/wireframes.pdf)  

---

## Features
### Existing Features

- **Navbar**   
    Each page features a responsive Materialize navbar that’s collapsed to a burger icon when viewing on smaller screens. The navbar has a hover effect so when the user hovers over the different pages the text changes color. In the left corner there is a logo with a link that takes you to the landing page.
    - Users that are not logged in have the following pages in the navbar:
        - HOME
        - RECIPES
        - SIGN UP
        - LOG IN  
    - Users that are logged in have the following pages in the navbar:
        - HOME
        - RECIPES
        - ACCOUNT
        - LOG OUT  
    - Admin that are logged in have the following pages in the navbar:
        - HOME
        - RECIPES
        - ACCOUNT
        - MANAGE CATEGORIES
        - LOG OUT  

- **Footer**  
    The footer is displayed on all pages and features links to social media accounts (currently to the main sites for the platforms but will eventually be linked to Yum Yum's social media accounts once they exist)

- **Home**  
    The landing page features a flat illustration picturing a woman feeding a baby that is sitting in her lap. There is also a call to action button with the text *show recipes* that leads to the page with all the recipes so that users have an easy and quick way of finding it.

- **Recipes**   
    The Recipe page features a search bar at the top and below are links to the different categories that the recipes are divided into so you can filter out the category you're intrested in. The recipes are presented in a grid with image cards.
    - **Search bar**  
    Allows the user to search for the name of a recipe or an ingredient in the recipe. This will then filter out all the recipes that includes the word that was searched.
    - **Cards**  
    On the front the user is provided with an image of the recipe followed by the category and then the name. There is also an hover effect when you move the cursor over the cards to highligt which recipe you're currently on. When you click on the card the recipe is displayed. If you're the user who has uploaded the recipe you also have the possibility to edit or delete it.

- **Account**   
On top of the Account page there is a button to Add a recipe and below is all the recipes uploaded by the user.
    - **Add Recipe**  
    As a registered user you can upload your own recipes. To do this you fill in a form that includes:
        - Recipe Category
        - Recipe Name
        - Ingredients
        - Instructions
        - Image

        All fields need to be filled out for the form to be submitted. The recipe is then displayed on the users own account page and on the recipe page.
    - **Edit Recipe**
    You can edit your own recipe. The form is prefilled with the information that you have filled out so it's easy to adjust any changes. 
    - **Delete Recipe**
    You can delete your own recipe. When you click on the delete button a confirmation modal pops up to assure you want to delete the recipe and not doing it accidentally.

- **Sign Up**  
The Sign up page features a simple form where the user can pick a username and a password. A request is made to MongoDB to check if the username is already in use. If it's not being used a profile is created and the user is directed to their account page.

- **Log In**  
The log in page also features a simple form where the user type their username and password to log in to their account. If the user doesn't exist or make a typo when writing, a flash message appears that says "Incorrect Username and/or Password".

- **Manage Categories**  
When site admin is logged in there is a page to manage the categories for the recipes. It's possible to either edit or delete the existing categories or to add new ones.


### Features Left To Implement  

- At the moment there are not so many recipes on the website but eventually it will be a lot more and it could become hard to navigate if everything is on one single page and that is why pagination would be a nice feature to have.
- To upload your own images of the recipe instead of an URL
- To save your favourite recipes
- To rate recipes
- The possibility for users to delete their own account
- Add more information about the recipes such as allergies, servings, preparation time and so on
- A more informative landing page that continues when you scroll with e.g top rated recipes, recipes for different ages or other tips that could be useful for parents  

---

## Database   

Diagram of my database:

![database](static/images/README/database.png)  

---  

## Technologies Used  

### Languages  

- HTML5, CSS3, Javascript and Python3

### Frameworks and Libraries  

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
- [pip](https://pip.pypa.io/en/stable/)
- [dnspython](https://www.dnspython.org/)
- [jQuery](https://jquery.com)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
- [Materialize](https://materializecss.com/) 
- [FontAwesome](https://fontawesome.com) 
- [Google Fonts](https://fonts.google.com) 

### All other tools  

- [MongoDB](https://www.mongodb.com/atlas/database) - used as database for this project
- [Heroku](https://dashboard.heroku.com/) - used to deploy the live site
- [GitPod](https://www.gitpod.io) - used for their IDE while building the website
- [GitHub](https://github.com) - used to store repository
- [Balsamiq](https://balsamiq.com) - used to create wireframes
- [DevTools](https://developers.google.com/web/tools/chrome-devtools) - used to test responsiveness 
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - used to improve performance
- [Tinypng](https://tinypng.com) - used to compress images
- [Freeformatter](https://www.freeformatter.com/) - used to beautify code
- [Coolors](https://coolors.co) - used to create color palette
- [dbdiagarm](https://dbdiagram.io/home) - used to create database diagram 
- [Am I Responsive](http://ami.responsivedesign.is/#) - used to create the mockup image in the beginning of this README file.
- [Canva](https://www.canva.com) - used to create the hero image and logo in navbar
- [RealFaviconGenerator](https://realfavicongenerator.net) - used to create site favicon
- [W3C Markup Validation Service](https://validator.w3.org) - used to check the HTML pages
- [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/) - used to check the CSS file
- [JSHint](https://jshint.com) - used to check the script.js file
- [PEP8 online](http://pep8online.com) - used to check the app.py file  

---

## Testing  

Testing information can be found [here](TESTING.md)  

---

## Deployment  

### Create Project  

This project was created on Github using the following steps: 
1. Navigate to [GitHub](https://github.com/) and sign in
2. On the left hand side above the list of your repositories click on the green button that says "New", this will create a new repository
3. From the drop down menu that says "Repository templates" I choose the Code Institute Template  
4. Enter a name for the project and then click on the green button that says "Create Repository"

Before creating the Heroku app you need to add the following files in Gitpod:

 - To create your requirements file, type this in the terminal:
    - pip3 freeze --local > requirements.txt
- To create your Procfile, type this in the terminal:
    - echo web: python run.py > Procfile 

In the Procfile make sure it contains the following line: web: python app.py, and that it is no blank line after it.

### Deployment to Heroku  

This project was deployed through Heroku using the following steps:
1. Navigate to [Heroku](https://dashboard.heroku.com/login) and sign in
2. On the top right corner there is a button that says "New". Click this button and choose the option "Create New App"
3. Choose a name for the App and what region that are closest to your location, click "Create App"
4. Click on the tab saying "Deploy" and select GitHub, Connect to GitHub
5. Enter the name of your repository on GitHub and click search
6. When the repository is found, click the "Connect" button
7. Click on the tab saying "Settings" and then click on the button saying "Reveal config vars"

8. Add these variables:

    key: IP, value: 0.0.0.0 <br>
    key: MONGODB_NAME, value: (the name of your database)<br>
    key: MONGO_URI, value: (unique uri from mongo.db)<br>
    key: PORT, value: 5000<br>
    key: SECRET_KEY, value: (unique secret key for configuration)<br>

9. Click on the "Deploy" tab and scroll down to the section "Automatic Deployment"
10. Choose the branch you want to deploy from and then click "Enable Automatic Deploys"

### How To Run The Code Locally  

To run this project locally you need to create the env.py file using your own variables since these are not provided for security reasons. To have the database connection you'll also need to create your own database collection on MongoDB and connect it to your project.

1. Log in to Github.
2. Navigate to the [repository](https://github.com/flisanp/ms3-baby-food-recipes)
3. Click the tab that says "Code" and from the dropdown menu choose copy Git URL
4. Open Git and type "git clone" in the terminal followed by the URL you just copied, press enter to create your local clone
5. To install the packages listed in the requirements file type the following in the terminal: 
pip install -r requirements.txt

### Fork Project  

To fork the project follow these steps:

1. Log in to Github
2. Navigate to the [repository](https://github.com/flisanp/ms3-baby-food-recipes)
3. Locate the "Fork" button on the top right corner of the page
4. A duplicate of the original repository is now in your Github account

---

## Credits

### Code

Changing the text color on navbar from [Stack Overflow](https://stackoverflow.com/questions/33746269/changing-the-text-color-on-a-nav-bar-using-materialize-css-rails)


404 error page from [this blog post](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)

Code that will fix the validation requirements for Materialize select elements, copied from Code Institue lesson: Materialize Form Validation

`def is_logged_in` - Function that returns None if the user isn't logged in otherwise returns the username, by mentor Reuben Ferrante

The lessons from The mini project by Tim Nelson

### Content  

Recipes that I've added comes from these websites (a few moderations were made on some recipes):  

[Banana Pancakes](https://babyfoode.com/blog/banana-pancakes-for-baby/)  
[Oatmeal Porridge](https://www.eatingbirdfood.com/oatmeal-for-babies/)  
[Fruit and Veggie Smoothie](https://www.theeverydaymomlife.com/recipe/hidden-veggie-smoothies-kids-will-actually-eat/)  
[Apple and Blueberry Puree](https://blog.homemade-baby-food-recipes.com/babys-blueberry-and-apple-puree/)  
[Zucchini Risotto](https://blog.homemade-baby-food-recipes.com/healthy-zucchini-risotto-for-baby/)  
[Pumpkin Soup](https://www.mylittlemoppet.com/easy-pumpkin-soup-recipe-babies/)  
[Chickpea Rice](https://www.mylittlemoppet.com/chickpea-rice-for-babies/)  
[Raspberry Chia Pudding](https://plantbasedjuniors.com/mango-chia-pudding/)  
[Mint and Pea Soup](https://www.ellaskitchen.co.uk/recipes/pea-green-soup)  
[Creamy Potato Soup](https://www.healthylittlefoodies.com/leek-and-potato-soup/)  

### Media

All images of recipes uploaded by me are sourced via [Unsplash](https://unsplash.com/)

[Banana Pancakes](https://unsplash.com/photos/tKKe3aDvncE)   
[Oatmeal Porridge](https://unsplash.com/photos/-eLS9k_uhUc)  
[Fruit and Veggie Smoothie](https://unsplash.com/photos/wjt2-Vo7GA8)  
[Apple and Blueberry Puree](https://unsplash.com/photos/QvMen4ChnoI)  
[Zucchini Risotto](https://unsplash.com/photos/qIPRTMulc-g)  
[Pumpkin Soup](https://unsplash.com/photos/QbCF4wzSjJw)  
[Chickpea Rice](https://unsplash.com/photos/vCNLO20cuwY)  
[Raspberry Chia Pudding](https://unsplash.com/photos/5fj-ShvSEnc)  
[Mint and Pea Soup](https://unsplash.com/photos/BA6FzJZ9IfY)  
[Creamy Potato Soup](https://unsplash.com/photos/rIxoNvlcg0o)  

Logo and hero image on landing page is from [Canva](https://www.canva.com/)  
Cherries vector is from [Vecteezy](https://www.vecteezy.com/free-vector/apple)  

---

## Acknowledgements

Special thanks to my mentor Reuben Ferrante for valuable feedback throughout the project
