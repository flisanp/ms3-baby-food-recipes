![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome flisanp,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

# Baby Food Recipes

[A live version of the page can be viewed here](https://flisanp.github.io/ms2-barcelona-guide/)

![mockup image](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/mockup-image.png)

This website is a city guide to Barcelona and aims to provide information about the city to users who are planning to visit or are currently visiting Barcelona. Users can navigate through Google Maps to get top picks for restaurants, tourist attractions, hotels and shops.

This website is a recipe site for baby food. Users can search trough existing recipes and create an account where they can upload their own recipes and share them with other users.


# UX

#### The Goals For This Website Is To: 
- Be user-friendly.
- Let users know about good restaurants, shops and hotels.
- Give users information about interesting places to visit during their stay.
- Provide a map with markers for users to easily navigate and find what they are looking for.
- Provide the citys weather forecast.
- Make it easy for users to share the site.

#### User Stories

1. As a new visitor to the website I would like to find good and healthy recipes that I can make for my baby.
![wireframe]()
2. As a user I want to be able to create an account where I can upload my own recipes.
![wireframe]()
3. As a user I want to be able to edit my recipes
![wireframe]()
4. As a user I want to be able to delete my recipes
![wireframe]()
5. As a user I want to be able to log in to my account
![wireframe]()
6. As a user I want to be able to search for different recipes
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
My main colors for the project is two different shades of blue, #11466A, and #127BF2, that are inspired by Gaudís mosaic which can be seen scattered over large parts of the city. In fact you can hardly talk about Barcelona without mentioning Gaudí and that is why I have choosen the iconic image over Parc Güell as a source for my color palette.

![color palette](https://github.com/flisanp/ms2-barcelona-guide/blob/master/readme%20assets/color-palette.jpg)

I wanted the design to be easily navigated and for the user to immidately understand what the purpose of the site is. I therefore choose to have a headline that clearly states that it is a travel guide to Barcelona and underneath that I have four call to action buttons with different categories depending on what you want to do in the city. The buttons are linked straight to a Google map and shows markers for different categories. Each category has it's own markers with icons that clearly states what category that have been clicked so that there will be no confusion when they're on the map. All markers open an info window when you click on them and in that info window you will find the name of the location followed by some further information about the place such as a link to their website which will make it easy for the user to get more information about places they find interesting. When you click on a new info window the previous one closes so that the map doesn't get cluttered. I wanted the map to be easy to navigate and that is why I choose to have it in full screen. 
I also wanted to have a weather forecast so that users can plan their packing and activities accordingly, this is located below the map but there is also a link called WEATHER in the navbar for users to easily find it at all time.

# Features

**Navbar** - Each page features a responsive Bootstrap navbar that’s collapsed to a burger icon when viewing on smaller screens. The navbar has an hover effect so when the user hovers over the different pages the text changes color. The same color is used to show which page the user is currently on. The navbar has links to the landing page *HOME* and the weather forecast *WEATHER*.

**Home** - The landing page features a hero image and on top of the image is a heading with the text "Barcelona city guide" to clearly state what the site is about. 
Underneath the heading are four *Call to action buttons* that are linked to a *Google map*. The map, which is the most significant feature on the site, is located undeneath the buttons and gives a view over Barcelona. When the user clicks on a button different *markers* appear on the map and every marker has an icon that clearly indicates which category the user is currently viewing. When the user clicks on a marker a *info window* opens where they can find the name of the location and the prime information. In every info window there is a link to the locations website so the user easily can find out more about the places they are interested in. When you scroll down the page a scroll to top button appears that gives the user a shortcut to the top of the page. 
In the bottom left corner the user can find a toggle *share button* that expands when they click it and provides the user  with several ways to share the site on different social media platforms. They also have the possibility to send it by mail or to print it. 

**Weather** - The *weather forecast* is located below the map and also reachable at all times through a link in the navbar. It's displaying a 7 day forecast over Barcelona with distinct icons which gives the user an indication of what the weather will look like the following week. To the left it displays the current weather.

**Footer** - Exists on the bottom of every page. Located in the center of the footer are four icons with links to the sites social media platforms. The links have the same hover effects as the navbar and changes color as you hover over them.

#### Features Left To Implement
Even though I wanted to have a clean site where you'll just find the top picks in every category there could be many more features added to provide the user with more functionality and to simplify their planning, for instance: 
- More locations on the map
- More categories such as beaches/nightlife/things to do with kids
- Book hotels/flights/tours through the site
- Timetables for tourist buses

# Technologies Used

- HTML5, CSS3 and Javascript
- [GitPod](https://www.gitpod.io) - The developer used GitPod for their IDE while building the website.
- [GitHub](https://github.com) - This project uses GitHub to store the projects code after being pushed from Git.
- [Bootstrap](https://getbootstrap.com) - This project uses Bootstrap to make the site responsive and to implement features such as the navbar and the buttons.
- [FontAwesome](https://fontawesome.com) - This project uses FontAwesome for social media icons.
- [Google Fonts](https://fonts.google.com) - This project uses Montserrat and Lora from Google Fonts.
- [Balsamiq](https://balsamiq.com) - The developer used Balsamiq to create wireframes.
- [DevTools](https://developers.google.com/web/tools/chrome-devtools) - The developer has used DevTools to test responsiveness and diagnose problems. The tool **Lighthouse** has been used to improve the website's quality. 
- [Tinypng](https://tinypng.com) - The developer used Tinypng for compressing images.
- [Freeformatter](https://www.freeformatter.com/) - The developer used Freeformatter for beautifying the code.
- [A11y](https://color.a11y.com) - The developer used Wave for checking the websites color contrast accessibility.
- [Wave](https://wave.webaim.org) - The developer used Wave for checking the websites color contrast accessibility. 
- [ResizeImage](https://resizeimage.net) - The developer used ResizeImage to resize images.
- [Coolors](https://coolors.co) - The developer used Coolors to create color palette.
- [Techsini](https://techsini.com/multi-mockup/index.php) - The developer used Techsini for creating the mockup image in the beginning of this README file.
- [InDesign](https://www.adobe.com/se/products/indesign.html) The developer used InDesign for creating the favicon.
- [Addthis](https://www.addthis.com) The developer used Addthis for the toggle share button.


# Testing

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

- Google Maps would not load.
    - InitMap being called in the `<body>` instead of as a callback function: `<body onload="initMap()">`

- Info window on markers only shows last location.
    - changed marker and infowindow to const types instead of var. They need to be const as per the google documentation.

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
2. Navigate to the [repository](https://github.com/flisanp/ms2-barcelona-guide).
3. Click the green GitPod button on the top right.
4. A new workspace will be created.

# Credits

#### Content

To find information about the best locations I've used the following sources:

[Time Out](https://www.timeout.com/barcelona)

[Condé Nast Traveller](https://www.cntraveler.com/destinations/barcelona)

**Code**

[Google Maps API](https://developers.google.com/maps/documentation/javascript/get-api-key)

[Google Maps tutorial for markers](https://developers.google.com/maps/documentation/javascript/adding-a-google-map)

[Google Maps tutorial for info windows](https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple)

Weather forecast API: [Visual Crossing](https://www.visualcrossing.com/weather-data)

Fixed width button: [Stack Overflow](https://stackoverflow.com/questions/11050269/fixed-width-buttons-with-bootstrap)

How to store icons for google map markers on local folder: [Stack Overflow](https://stackoverflow.com/questions/12652287/using-a-local-folder-how-to-store-google-markers)

Scroll to top button: [w3schools.com](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)


#### Media
- Image on landing page by [Camille Minouflet on Unsplash](https://unsplash.com/@caminouflet)
- Image on contact page by [Vitor Monteiro on Unsplash](https://unsplash.com/@vitorhugomonteiro) 
- Icons for markers on map from [Map icons](http://map-icons.com)
- Favicon made by me

#### Acknowledgements

- To tutor support for guiding through bug issues
- To mentor Sinead O'Brien for helpful feedback


<a target="_blank" href="https://icons8.com/icon/5Rd0v9hlYljM/baby-food">Baby Food</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
