# Baby Food Recipes

[A live version of the page can be viewed here](https://baby-food.herokuapp.com/home)

![mockup image]()


This website is a recipe site for baby food. Users can search trough existing recipes and create an account where they can upload and store their own recipes and share them with other users.


## UX

### The Goals For This Website Is To: 
- Provide a place where people can easily find good and healthy recipes for babies
- Be able to create an account to store your own recipes
- Share baby food recipes with other people
- Make it easy for users to navigate the site on any device 

### User Stories

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

#### Design 

![color palette]()


# Features

**Navbar** - Each page features a responsive Materialize navbar that’s collapsed to a burger icon when viewing on smaller screens. The navbar has a hover effect so when the user hovers over the different pages the text changes color. The navbar has links to the landing page *HOME*, recipes page *RECIPES*, registration page *SIGN UP* and login page *LOG IN*. When you are logged in the navbar has a link to your profile page *ACCOUNT* and when Admin is logged in there is also a link to a page for managing the categories *MANAGE CATEGORIES*.

**Home** - 

**Recipes** - 

**Footer** - Exists on the bottom of every page. Located in the center of the footer are four icons with links to the sites social media platforms. 

#### Features Left To Implement


# Technologies Used

## Languages used
- HTML5, CSS3, Javascript and Python3

## Frameworks, Libraries & Programs Used
- [GitPod](https://www.gitpod.io) - used GitPod for their IDE while building the website.
- [GitHub](https://github.com) - This project uses GitHub to store the projects code after being pushed from Git.
- [Materialize](https://materializecss.com/) - used to make the site responsive and to implement features such as the navbar and the buttons.
- [FontAwesome](https://fontawesome.com) - for social media icons.
- [Google Fonts](https://fonts.google.com) - This project uses Montserrat and Lora from Google Fonts.
- [Balsamiq](https://balsamiq.com) - to create wireframes.
- [DevTools](https://developers.google.com/web/tools/chrome-devtools) - to test responsiveness and diagnose problems. The tool **Lighthouse** has been used to improve the website's quality. 
- [Tinypng](https://tinypng.com) - for compressing images.
- [Freeformatter](https://www.freeformatter.com/) - used for beautifying the code.
- [A11y](https://color.a11y.com) - used to check the websites color contrast accessibility.
- [Wave](https://wave.webaim.org) - used to check the websites color contrast accessibility. 
- [ResizeImage](https://resizeimage.net) - used to resize images.
- [Coolors](https://coolors.co) - used to create the color palette.
- [Techsini](https://techsini.com/multi-mockup/index.php) - used to create the mockup image in the beginning of this README file.
- [Canva](https://www.canva.com) used to create the hero image and logo in navbar.

# Deployment
### Create Project
To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:
1. Navigate to Github[GitHub](https://github.com/) and sign in
flisanp repositories.
2. Select the one that is called ms2-barcelona-guide from the list.
3. Click on settings in the menu that is located to the top right.
4. Scroll down to "GitHub Pages"
5. Under "Source", Select Master Branch from the drop-down menu.
6. Click Save and the website is now deployed.

### Deployment to Heroku
This project was deployed through Heroku using the following steps:

1. Navigate to Heroku[Heroku](https://dashboard.heroku.com/login) and sign in
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
