# Poster Bay | E-Commerce Site for Posters

## Index:
* <a href="#project-background">Project Background :information_desk_person:</a>
* <a href="#ux">UX :iphone:</a>
* <a href="#features">Features :clipboard:</a>
* <a href="#technologies">Technologies Used :wrench:</a>
* <a href="#testing">Testing :flashlight:</a>
* <a href="#deployment">Deployment :rocket:</a>
* <a href="#credits">Credits :pencil2:</a>

---
<span id="project-background"></span>
## Project Background :information_desk_person:

Poster Bay was founded by 1 artsy gal looking to provide other art-loving folks with affordable, high quality prints from some of the world's iconic artists. Each print has been carefully curated & printed on 170gsm Silk paper to be long-lasting.

Through this ecommerce site, customers are able to view a variety of poster prints, purchase them and store their information on the site to make their checkout flow much quicker the next time they visit the website. 

---

<span id="ux"></span>
## UX :iphone:

### 1. Who is this website for?

This website is for anyone interested in buying high-quality art prints from iconic artists, although judging by the type of works, it would seemingly appeal to a younger demographic between the ages of 16-35 years. 

### 2. First-Time User Goals:

* As a First Time Visitor, I want to easily understand the main purpose of the site and who the company is.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content most relevant to me.
* As a First Time Visitor, I want to be able to register my profile.
* As a First Time Visitor, I want to be able to access my profile once registered. 
 As a First Time Visitor, I want to be able to receive an email confirmation after I register 


### 3. Returning Visitor Goals

* As a Returning Visitor, I want to be able to log in to my profile with the credentials that were registered.
* As a Returning Visitor, I want to be able to log out of my profile.
* As a Returning Visitor, I want to be able to get a variety of product options.
* As a Returning Visitor, I want to be able to see and access my order history.
* As a Returning Visitor, I want to be able to access my profile.
* As a Returning Visitor, I want to be able to easily recover my password in case I forget it 
* As a Returning Visitor, I want to be able to to get in touch with the company for support when needed

### 4. Frequent User Goals

* As a Frequent Visitor, I want to check to see if there are any newly added products that have been added on the website.
* As a Frequent Visitor, I want to be able to log in & log out of my profile with ease.

### 5. Shopper Goals

* As a Shopper, I want to be able to View a list of products so that I can Identify the price, description, and product image
* As a Shopper, I want to be able to View individual product details so that I can make an informed decision about the product 
* As a Shopper, I want to be able to Easily view the total of my purchases at any time so that I can Stay within my allocated budget 
* As a Shopper, I want to be able to Sort the list of available products so that I can Identify the prints based on a specific artist or design 
* As a Shopper, I want to be able to Search for a product by name or description so that I can quickly Find a specific product I'd like to purchase
* As a Shopper, I want to be able to Easily see what I've searched for and the number of results so that i can Quickly decide whether the product I want is available 
* As a Shopper, I want to be able to Easily select the quantity of the a product when purchasing it so that I can Ensure I dont select the wrong quantity 
* As a Shopper, I want to be able to Easily add or remove products from the cart  so that I can Have flexibility in changing my order in the chance that I don't want a specific product or want to add more products to my cart

### 6. Site Admin Goals

* As a Site Admin, I want to be able to Add an item to my store so that I can keep providing customers with new options 
* As a Site Admin, I want to be able to Edit an item so that I can Easily change product prices, description, image, and other product-related info
* As a Site Admin, I want to be able to Delete an item so that I can Easily remove an item from my store when its out of stock 
* As a Site Admin, I want to be able to view and manage all orders so that I can ensure customers are able to checkout smoothly 

### Design:

I opted for a clean & minimalistic but modern look & feel for this website. The background is kept white to allow for the colorful imagery of the posters to stand out, while the buttons are given a bright yellow hover effect to add a fun and young element to the website.

* Color Scheme:
  * The main colors used are Black, White, Yellow and pops of bright pink.

* Typography:
  * All Headers use Inconsolata, a sans-serif font with nice letter-spacing - to give the website an artistic and fun kind of comic book touch.
  * Montserrat is my secondary font, used for paragraphs. It has a lighter font-weight, which pairs nicely with other sans-serif fonts and is easy to read on smaller devices.
  * Sans-Serif is used as the backup font for both Inconsolata and Montserrat to stay consistent with the font-family. 

* Imagery:
  * A bright, colorful abstract image is used for the hero image to be eye-catching & inviting to the user and stay consistent with the “modern/contemporary” art theme.
* The artworks for the posters speak for themselves - they are eye-catching, fun, young and really enticing choices to use as posters in one’s home. 

### Wireframes & Mockups:

* View website wireframes for desktop & mobile [here](https://drive.google.com/file/d/1I_eR45ittdz8OyTWI3xFV8nl4pDpnovN/view?usp=sharing)
---

<span id="features"></span>
## Features :clipboard:

The site contains certain features which are not visible or available to unregistered/logged out users. 
### Features visible to All Users:
* **Shop All Products**
   * * The Shop page contains an assortment of products sold by Poster Bay. Each product card displays an image of the item, the name, artist name, price and a CTA button to view the product. This page also contains a search bar and filters to allow users to quickly find a product based on search query, artist or design.
* **Register**
   * The register feature is one visible to all users as a link on the navigation bar. Once clicked, it leads to a form where users can create a unique username and password. If the username is already taken, an error message will flash indicating to the user they should login or use a different email. Once the user has registered successfully, they will be redirected to the homepage. A success message also flashes at the top of the page signalling a successful registration.
* **Login**
   * The login feature is also visible to all users and can be found in the navigation bar. It enables users who already have a profile to login with their credentials. If the credentials don't match those entered during registration, an error message “Incorrect Username and/or Password” will flash across the screen. For users who have not registered yet, a CTA link at the bottom of the form directs them to register. Alternatively, if the login is successful and the username & password match those stored in the database, a welcome message will flash & the user will be redirected to the homepage.
* **Product Details Page**
   * The product details page retrieves information about the item including artist, short product description, and price. The user can also update the quantity here. Buttons at the bottom allow users to add the product to the cart or keep shopping. 
* **Cart Page**
   * Users can access the cart via the top navbar. If they have products, these will be displayed here, if not a message will appear telling them their cart is empty and direct them to the shop page. If there are products, users can update the quantity or even remove the products from their cart. Each time an action is taken a notification message gives them feedback. 
* **Toast Messages**
   * Bootstrap toasts have been added to give users feedback whenever an action is taken such as adding products to cart, removing them, logging in, checking out and so on. These messages appear on the upper right hand of the screen. 
   * A special toast was added for adding items to the cart, as it displays the items added and allows users to go directly to the checkout.
* **Checkout Page**
   * The order checkout page is where users go to from the cart page. Here they can fill out the form with all shipping details and make their payment. They are also able to see the contents of their bag displayed. If the user is not logged in, they will see under the form options to register or login to be able to save their details for the next time they make a purchase. 
* **Footer**
   * Located at the bottom of each page of the website, the footer consists of a contact us section with an email address, a short about section, and social media links leading to art accounts intended to give users more inspirations of where to put up posters.
* **Navbar**
   * The navigation bar at the top of each page of the website enables the user to easily access all pages of the website. On smaller devices, the navbar transforms into a burger menu, where links are only visible in a dropdown menu. There are two different views of the navigation bar - one view to all users, and the other to those users who are logged in to the website.

### Features visible to Logged In/Registered Users:
* **Profile**
   * When a user logs into their account, they are redirected to the Profile page, which is specific to that individual user. Upon entry, the user can see a form where they can update their shipping details. If they selected the checkbox save info in the checkout, the form will be populated with the info they put in. At any point the user can update this form and it will also update the form in the checkout flow. Here they can also see their order history of past purchases used with their current account. 
* **Logout**
   * The logout link is only visible to users who are logged in to the website. Located in the top navbar, it provides users to easily log out of their session
* **Save Shipping Details Info**
   * The Save Shipping Details Info checkbox is located on the checkout page and can be ticked by users if they want to save their info to their profile. It is only available to users who are logged in.
* **Product Management**
   * The product management functionalities are only accessible to the admin of the website, who has to be logged into the website. The admin can access it via the top navbar and upon entry can proceed with adding new products, editing and deleting products. 


### Features to implement in the Future

* Functionality to let users save items to their wishlist 
* Function to allow user to comment under each product and leave their review 

---
<span id="technologies"></span>
## Technologies Used :wrench:

### 1. Languages

This Full Stack Project focused on the use of the following languages:
* HTML5 - for website structure
* CSS3 - for styling
* JavaScript - for running interactive features
* Python for automating tasks & scripting
* JQuery
* Django - a high-level Python framework 
* Heroku - for deploying the project 

### 2. Other Programs & Frameworks Used

* FontAwesome - for all icons used on the buttons
* Balsamiq - for creating wireframes
* Bootstrap 4.4.1 - for assisting in responsiveness and layout of website
* Stripe - Payment solution

### 3. IDE's

This website was developed on GitPod.

### 4. External Hosting

This website is saved in a repository on GitHub.

---

<span id="testing"></span>
## Testing :flashlight:

### 1. Testing Tools

* [The W3C Markup Validation Service](https://validator.w3.org/) - for testing my HTML code
  * Result: No errors
* [The W3C CSS Validation Service: W3 Jigsaw](https://jigsaw.w3.org/css-validator/) - for testing my CSS code
  * Result: No errors
* Chrome Dev Tools - for testing:
  * Mobile responsiveness
  * CSS styling changes before implementing it in the code
  * Network to assess whether it was picking up Javascript (status: 200)

### 2. Testing User Stories (UX Section)

### A. First-Time Visitor Goals:

* As a First Time Visitor, I want to easily understand the main purpose of the site and who the company is.
   * Upon entering the site, users are presented with a bright, catchy and easily readable banner image, which introduces the Company name and purpose of the site.
   * In the footer, a short about us blurb gives the user further details about the company & its mission.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content most relevant to me.
   * The website is designed to be very clean and straight to the point. The navigation bar enables the user to visit different pages on the website with ease. CTA buttons also link to relevant content, pages & functions.
* As a First Time Visitor, I want to be able to register my profile.
   * The user is able to register via the navigation bar. If they accidentally click on Login, a link at the bottom of the form also redirects the user to the register page.
* As a First Time Visitor, I want to be able to access my profile once registered.
   * The user is able to access their profile via the navigation bar.
* As a First Time Visitor, I want to be able to receive an email confirmation after I register 
   * After registering, the user is redirected to an email verification page which triggers an email to the registered email with the link to verify their email and login. 

### B. Returning Visitor Goals

* As a Returning Visitor, I want to be able to log in to my profile with the credentials that were registered.
   * Users can login easily via the navigation bar with their credentials.
* As a Returning Visitor, I want to be able to log out of my profile.
   * Once in session, users can log out of the website via a link in the navbar. This will lead to a confirmation sign out page in case they accidentally clicked logout without the intention of logging out. Once confirmed it will lead back to homepage 
* As a Returning Visitor, I want to be able to get a variety of product options.
   * Via the navbar, the section “Shop” allows the user to scroll through the array of product options 
* As a Returning Visitor, I want to be able to see and access my order history.
   * Once in session, the user can visit their profile page, via the navbar, to see and access their order history.
* As a Returning Visitor, I want to be able to access my profile.
   * Once in session, the user can access their profile via the top navbar.
* As a Returning Visitor, I want to be able to easily recover my password in case I forget it 
  * Upon clicking on login, the user will come to the login page which will have a link to recover password if forgotten and reset it 
* As a Returning Visitor, I want to be able to to get in touch with the company for support when needed
   * Users searching for support can look to the footer for the company’s contact details 

### C. Frequent Visitor Goals

* As a Frequent Visitor, I want to check to see if there are any newly added products that have been added on the website.
   * At this point the user is familiar with the layout of the website & can recognize new products that have been added.
* As a Frequent Visitor, I want to be able to log in & log out of my profile with ease.
   * The user is also familiar with the placement of the login and logout buttons located in the top navbar.

### D. Shopper Goals 

* As a Shopper, I want to be able to View a list of products so that I can Identify the price, description, and product image
   * All products are displayed clearly on the Shop page 
* As a Shopper, I want to be able to View individual product details so that I can make an informed decision about the product 
   * All product cards contain a button leading the product details page, where the product is presented to the user in great detail.
* As a Shopper, I want to be able to Easily view the total of my purchases at any time so that I can Stay within my allocated budget 
   * Once the shopper adds a product to the cart, the bag in the upper right corner in the navbar will display the total of their order. A notification also shows what’s in their cart and the price. 
   * A 3rd option for the user is to click on the bag icon in the navbar which will direct them to the cart page where all items will be displayed.
* As a Shopper, I want to be able to Sort the list of available products so that I can Identify the prints based on a specific artist or design 
   * Filters located in the Shop page allow the user to choose their desired “filter” from the drop down menus. This will filter the products based on what the user has selected. 
* As a Shopper, I want to be able to Search for a product by name or description so that I can quickly Find a specific product I'd like to purchase
   * A search bar located in the Shop page allows the user to search for their desired print by the keyword entered 
* As a Shopper, I want to be able to Easily see what I've searched for and the number of results so that i can Quickly decide whether the product I want is available 
   * Based on their query in the search bar on Shop page, the page will be updated with only the products relevant to their search 
* As a Shopper, I want to be able to Easily select the quantity of the a product when purchasing it so that I can ensure I don’t select the wrong quantity 
   * In both the product details page and in the cart, users are able to update their quantity easily 
* As a Shopper, I want to be able to Easily add or remove products from the cart  so that I can Have flexibility in changing my order in the chance that I don't want a specific product or want to add more products to my cart
   * In the cart, users can remove products from the cart, update their quantity, or even go back to the shop page to add more products to their cart 

### E. Site Admin Goals 

* As a Site Admin, I want to be able to Add an item to my store so that I can keep providing customers with new options 
   * The Site admin can add items to their store via the product management admin page via the top navbar 
* As a Site Admin, I want to be able to Edit an item so that I can Easily change product prices, description, image, and other product-related info
   * The Site admin can edit items to their store via the product management admin page via the top navbar 
* As a Site Admin, I want to be able to Delete an item so that I can Easily remove an item from my store when its out of stock 
   * The Site admin can delete items to their store via the product management admin page via the top navbar 
* As a Site Admin, I want to be able to view and manage all orders so that I can ensure customers are able to checkout smoothly 
   * The Site admin can access order history via Django admin, where all order history is stored in detail 


### 3. Further Testing

This website has been tested by friends and family to check for:
* bugs or disabled links
* clear user experience & navigation
* picture loading speed
* login/register/logout functionalities
* edit, add, delete items functionalities
* correct Toast message displays

### 4. Browser & Device Testing

This website has been tested on the following Desktop devices:
*  MacBook Pro 2013 - Chrome & Safari
*  Microsoft Edge - Chrome

This website has been tested on the following Mobile/Tablet devices:
* iPhone 11 - Safari
* iPhone 6 - Safari
* iPhone 6s - Safari
* iPad Air 2 - Safari

### 5. Bugs & Problems

During testing it was found that Webhook handler response fails even though order is processed and appears in both Stripe developer portal and in Admin displaying a 400 error.
Due to time restraints, I was not able to investigate deeper. 

---

<span id="deployment"></span>
## Deployment :rocket:

### Deployment to Heroku

This project was deployed to Heroku by following the steps below:
1. Create a requirements.txt by typing in the terminal command line: pip3 freeze --local > requirements.txt
2. Create a Procfile by typing in the terminal command line with: echo web: python app.py > Procfile.
3. Remove the trailing whitespace in the Procfile.
4. Type in the commands in the terminal: git add -A, Git commit -m "Your message" & Git push to push these changes into GitHub.
5. Navigate to the [Heroku website](https://dashboard.heroku.com/apps)
6. Create a new app by selecting the button labelled “New” on the dashboard and give the app a unique name.
7. Select the region you're situated in.
7. In the Deploy tab, select Github. Make sure you're connected to the right account.
8. Type in the name of the repository you wish to connect to
9. In the Settings tab, click on Reveal Config Vars and set as below:
   * IP = 0.0.0.0
   * MONGO_DBNAME = [name of your MongoDB]
   * PORT = 5000
   * MONGO_URI = unique link to your Mongo database
   * and finally your SECRET_KEY.
10. Once added, click "Hide Config Vars"
11. Navigate to the Deploy tab and select Enable Automatic Deploys.
12. At the bottom of the page, click on Deploy Branch, ensuring the master branch is selected.

### Forking the GitHub Repository
Forking the GitHub Repository creates a copy of the original repository in our GitHub account to view and/or make changes without affecting the original repository. This can be done through the following steps:

1. Log in to GitHub and find the GitHub Repository
2. At the top of the Repository - just above & to the right of "Settings" on the menu, locate the "Fork" Button.
3. Click this to create a copy of the original repository in your GitHub account.

### Live Site
* This website is stored in a repository on [Github](https://github.com/ZahraSadiq/Milestone2-AntwerpHotSpots.git)
  * It was developed on GitPod, with changes regularly pushed to GitHub's repository using one main master branch.
  * Both the deployed and developed versions of this website are identical.

This site is hosted on Heroku.
* You can view the live site [here](https://house-of-masala.herokuapp.com/)
* The url for the site is: https://house-of-masala.herokuapp.com/

---
<span id="credits"></span>
## Credits :pencil2:

### 1. Code Snippets

* The code in this project largely follows The Boutique Ado project by Code institute.

### 2. Media

* Icons from: [FontAwesome](https://fontawesome.com/icons?d=gallery)
* [Banner image](https://www.unsplash.com/)
* Poster images were sourced from:
   * [David Bowie Print](https://i.pinimg.com/564x/08/78/1e/08781e7bb532139e55c3185543d51baf.jpg)
   * [Banana Print](https://i.pinimg.com/564x/25/bf/32/25bf329b7bc5b8a726194038beeb1640.jpg)
   * [Campell’s Soup](https://i.pinimg.com/564x/42/ae/ef/42aeefbe857247449b30001124a8f1d8.jpg)
   * [Wonder Woman](https://i.pinimg.com/564x/45/90/46/459046e720d66645192942efc1a40e06.jpg)
   * [We're Not in Kansas Anymore Print ](https://malcolmsmithart.com/products/copy-of-dotty-in-sobe-45x30)
   * [Pow Print ](https://i.pinimg.com/564x/af/d7/85/afd7854e7a3880e7361d0bb9633d663a.jpg)
   * [Love Print ](https://i.pinimg.com/564x/14/45/1c/14451c499d4c8f30b9d151417d261f57.jpg)
   * [Widewalls Print ](https://i.pinimg.com/564x/64/bf/2a/64bf2af831a0ea6eb7269bfed6375ec8.jpg)
   * [Dancing Dog Print ](https://i.pinimg.com/564x/f5/bd/93/f5bd93a8edfb99791dfb5f256a422b8c.jpg)
   * [Studio View Print ](https://i.pinimg.com/564x/d7/b2/3a/d7b23a5ceccf54cd07bc4e3cbb04e689.jpg)
   * [Pool Print ](https://i.pinimg.com/564x/c9/be/9f/c9be9f4b3b269a066bd643421ef0abaa.jpg)
   * [Down the Winding Road Print ](https://i.pinimg.com/564x/7f/14/98/7f149842ba042dc6b1491c6b0aa46d74.jpg)
   * [Sunflower Print ](https://i.pinimg.com/564x/28/8d/69/288d6983068a379c9a6ba006f181bab2.jpg)
   * [Skulls & Sunflowers Print ](https://i.pinimg.com/564x/c5/7c/7f/c57c7fd5f929157a1b6b9624b5c3b2a1.jpg)
   * [Landscape Print ](https://i.pinimg.com/564x/e7/b4/fa/e7b4fa2032bcf81c27ed6c57657bef7b.jpg)
   * [Love Is The Answer Print ](https://i.pinimg.com/564x/cd/fb/b9/cdfbb9d14be2bd912e1fdc2b941b668c.jpg)
   * [Flower Thrower Print ](https://i.pinimg.com/564x/76/5d/8c/765d8c4adb32fbf4b1fab4ffd820958b.jpg)
   * [Man With Crown Print](https://i.pinimg.com/564x/a5/7c/8b/a57c8bc669b901f9a34d6d5ac694be6b.jpg/)
   * [Self Portrait Print ](https://i.pinimg.com/564x/5e/55/2a/5e552a90cfd7a4b17660694359d45806.jpg)
   * [Glowing Pumpkin Print ](https://i.pinimg.com/564x/ac/9e/43/ac9e43ba5777228cf91c70782c5ce020.jpg/)
   * [Fan Work Print ](https://i.pinimg.com/564x/4c/30/b8/4c30b8d70beb9f5fdc47fadfa5426040.jpg)

 ### 4. Acknowledgements

* **Oluwafemi Medale (My CI Mentor):** Thanks for your advice and support.
