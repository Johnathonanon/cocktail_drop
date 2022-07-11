# Cocktail Drop E-commerce Website

Cocktail Drop is a fully-functioning, interactive web application built using django, postgresql, bootstrap, stripe for payments, and deployed to heroku. Cocktail Drop is designed as a fullstack e-commerce website, with both front and back end functionality. The purpose of Cocktail Drop is to allow users to order a selection of cocktails online to be delivered to them at home. Currently, the site has an 'inventory' of 44 cocktails, and delivers to the areas of Dublin 1, 2, 4, 6, 7, 8, and 12. Delivery is a flat rate of €5 or free on orders over €100. Users can sign-up, log-in, review cocktails. rate cocktails, view previous orders, and of course order cocktails for delivery, specifying a desired time and date. Users can also choose to save their delivery information to their profile for futute orders. A review and rating can only be left once per user, and these are diplayed on the product page, so as to allow users to express their opinions on the different cocktails. The site also has a blog section, in which the site owner can create a post for users to view. The purpose of this section is for the site owner, and the employed mixologists to share tips, tricks and even just interesting trivia with people who may be interested.



The live link can be found here - https://cocktail-drop.herokuapp.com/

AmIResponsive snip

![Picture of AmIResponsive snip](media/amiresponsive.png) 

## How to use the Web Application

The web application is used by users who wish to order a selection of cocktails for home delivery. Orders can be placed by anonymous users, however a user must have an account in order to review and rate products, as well as saving their delivery details and order history. This is done by clicking the "Register" button in the right hand corner of the header. Once done so, the user can log into their account and benefit from the additionally functionality. As a site owner, signing in allows the addition/editing/deletion of products and blogposts.

An agile approach was taken in development and a total of 28 user stories completed during the process. These can be found at: https://github.com/Johnathonanon/cocktail_drop/projects/1

## Marketing
A Facebook business page was set up for this business and can be found at: https://www.facebook.com/Cocktail-Drop-102099425886207/

![Picture of Facebook 1](media/facebook_1.png)
![Picture of Facebook 2](media/facebook_2.png)
![Picture of FAcebook 3](media/facebook_3.png)

## Features

### Existing Features

- **User Walkthrough**

The user is greeted with the home page intially. The header contains the logo on the left hand side, which if clicked brings the user back to the homepage. On the right hand side of the header we have the navbar, which includes Blog, Products, My account, and Cart. The Blog nav item brings the user to the blog portion of the site and is somewhat self explanatory, the Products and My account nav items are dropdown menus, and allow the user a greater level of accuracy in which category of products they view, as well as extra functionality depending on whether they are logged in or not, or are a superuser. The last nav-item is the Cart, which apart from navigating the user to the 'cart' page, also updates with a running total, and changes colour as the user adds items to their cart. Underneath the navbar is the search bar, which allows the user to enter a search term and the results are queried against the products name and description and a list of relevant products populated for the user to view. 

The rest of the home page consists of a free delivery banner, alerting the user to the free delivery threshold, as well as a number of text boxes. The first is a welcome to the site and a description so users recieve immediate information about the site, the second invited users to view the 'menu' and is prepended by a button linking to the products page, the third is an invitation to view the blog with a corresponding button, and the last a short list of reviews.

The footer then contains social media links, a newsletter subscription form, and a link to the sites privacy policy. No cookies are used on the site, so it was decided this was adequate.

The header/navbar and footer are present on every page of the site, allowing the user ease of navigation.

This site uses django messages in order to alert the user to various things throughout the site.

![Picture of Index Page 1](media/index_snip_1.png)
![Picture of Index Page 2](media/index_snip_2.png)
![Picture of Product Dropdown Nav](media/product_dropdown.png)
![Picture of Account Dropdown 1](media/account_dropdown_snip_1.png)
![Picture of Account Dropdown 2](media/account_dropdown_snip_2.png)
![Picture of Cart Nav](media/cart_nav.png)

The account functionality comes from all-auth and therefore contains the associated security/functionality. The all-auth templates were customised to match the site but the base logic is all-auth, including email confirmation, form validation etc.

![Picture of Login form](media/sign_up.png)
![Picture of Signup form](media/login.png)

The Products page is populated with cards featuring all the available products in the database. The default sorting is highest rating first however this can be further sorted based on the users preference. The card displays the product name, price, category, and rating based on the average_rating product model function. It also contains the options to edit and delete if the user is signed in as an admin. The products page contains a 'back to top' button allowing the user to quickly reach the top of the page again without scrolling.

![Picture of All products page](media/all_products.png)
![Picture of Product sorting](media/sorting.png)

The product details page contains a image of the product, a container with name, price, category, rating, and description. Underneath the description is a quantity which aloows the user to add up to 20 of item to their cart. It also contains two buttons, allowing the user to rate and review the product respectively. These buttons do not appear unless the user is signed in. The user may only rate/review a product once and will receive a warning and redirect if they attempt to do so again. They will also recieve a message alering them when they are rating/reviewing a product, and thanking them afterwords. This page alos contains the ability for an admin to edit delete the product. The user can choose to return to the products page or confirm addition of the product to their cart.
At the very bottom of the page is a container displaying user reviews of the product. A message notifies users when an item is added to their cart, shows a cart preview, and allows them to navigate to the cart page.

![Picture of Product details 1](media/product_details_1.png)
![Picture of Product details 2](media/product_details_2.png)
![Picture of Product details logged out](media/logged_out_product_details.png)
![Picture of Product already rated message](media/already_rated.png)
![Picture of Product already reviewed message](media/already_reviewed.png)
![Picture of Product rating thanks](media/rating_thanks.png)
![Picture of Product review thanks](media/review_thanks.png)
![Picture of Cart update message](media/cart_message.png)

The cart page displays a table of the items currently in the cart, including product info, price, quantity, and subtotal. The quantity can be updated or item deleted from the cart. A total, delivery cost, and grand total are also displayed as well as a reminder for the user of the free delivery threshold. The user can navigate back to products or continue to checkout. If the user navigates to this page with no items selected they receive a message notifying them they have nothing in their cart.

![Picture of cart](media/cart_snip.png)
![Picture of empty cart](media/cart_empty.png)

The checkout page contains an order form which can be pre-populated if the user is logged in and wishes to do so, an order summary, and a stripe payment form. This form is fully validated.

![Picture of checkout page](media/checkout_snip.png)

Once an order is placed, a loading spinner disables the user from interacting with the page until the payment succeeds or fails, and the user then receives an order confirmation, which is also added to their order history, or the may attempt payment again.

![Picture of order confirmation](media/order_confirmation.png)

The users profile page, which is navigated to through the My Account dropdown displays a form allowing them to set/update their default delivery details, as well as an order history, from which they can view previous orders.

![Picture of Pofile page](media/my_profile.png)

As previously mentioned the site owner possesses the ability to add, edit, and delete product. This is done through the 'product management' section on the my account dropdown when signed in as admin, and the product page/product details page.

![Picture of add product page](media/add_product.png)
![Picture of edit product page](media/edit_product.png)

They also possess the ability to create, edit and delete blog posts. And the site users have the ability to view these posts via the nav menu.

![Picture of Blog page](media/blog_posts.png)
![Picture of blog details](media/blog_details.png)
![Picture of create blog page](media/create_blog.png)
![Picture of edit blog page](media/edit_blog.png)


- **Back End**

  - There are a variety of models used in this application, some of these are personally created, some modified versions of django example models or models from walkthrough projects (boutique ado).
  Models include Product, Rating, Review, UserProfile, Order and OrderLineItem(BA), and Post.
  Many of these models are subsequently used to populate forms i.e. Product, Rating, Review, Order, and allow the site user/owner to modify the site in certain ways as well as allowing the user to palce orders, owner to add products etc.

  - The site usues postgresql in production and sqllite3 in development. It has full crud CRUD functionality for various models.


### Features Left to Implement

- I would like for users to interact more with blog post, for example the ability to 'like' and leave comments 

- It would be a future goal to implement a 'favourite' system, allowing users to create a list of their favourite cocktails that they can come back to and use to make orders. 

- I would like to update the delivery time and date section of the order form, as it is it allows the user to place an order for delivery at a selected time/date but this would need ot be overhauled in production. I would hope ot implement a one per order unique availibility timeslot for each order, this would ensure that a large number of order would not be placed for the same timeslot and cause issues.

- I would like to limit number of items per order. Since this is a make on demand product, taking time and ingredients, it would be very easy for a large number of orders to be placed and overwhelm the site owners ability to actually produce the product.

## Testing
The application has been consistently tested throughout its development by both myself and others. The gender and age of testers varied, with age ranging from 20s to 60s and testers having a diverse range of computer knowledge, and each tester found the application intuitive and easy to use.
 
Several bugs were found in development but all were corrected to the best of my knowledge at the submission of this project. These included one particular issue with product cards duplicating on the products page upon submission of a rating. This was solved using: products = list(set(list(products))), but I'm not sure what the underlying issue was, and unforunately I wasn't able to spend as much time troubleshooting as I would like.

A small amount of automatic testing was done, but again, due to time constraints this was in my opinion not enough and I would have preferred to do far more. However the site was fully tested and found working as intended, so I am content in this instance.

All code was passed throught the PEP8 linter and passing ok. Any remaining errors are long line etc. and do not effect the functionality of the code, and I chose to leave most as they caused issues when attempting to rectify.

### Validator Testing

PEP8 linter - http://pep8online.com/

### Unfixed Bugs

- Unaware of unfixed bigs at time of submission

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:
  - Create a heroku account
  - Select create new app on heroku dashboard, and fill out necessary requirements (name, etc.).
  - Select to add postgresql databse to app.
  - Once app is created, navigate to 'settings'. Set your config vars ie. database url, secret key. 
  - Next navigate to 'deploy'. For this project the deployment method chosen was Github. The relevant github account and repository must be connected and then either manual or automatic deployment chosen.
  - Once the app is succesfully built it will then be deployed and be 'live'

## Requirements
- The following were used in this project
  - asgiref==3.5.2
  - cloudinary==1.29.0
  - crispy-bootstrap5==0.6
  - dj-database-url==0.5.0
  - dj3-cloudinary-storage==0.0.6
  - Django==3.2
  - django-allauth==0.51.0
  - django-crispy-forms==1.14.0
  - gunicorn==20.1.0
  - oauthlib==3.2.0
  - Pillow==9.1.1
  - psycopg2==2.9.3
  - PyJWT==2.4.0
  - python3-openid==3.2.0
  - pytz==2022.1
  - requests-oauthlib==1.3.1
  - sqlparse==0.4.2
  - stripe==3.5.0


The live link can be found here - https://cocktail-drop.herokuapp.com/

## Credits

I am grateful to the Code Institute tutors for their patient help with this project. Without them it would not have gone nearly so smoothly.

My mentor was very helpful and his knowledge and experience is highly appreciated.

Many elements of this project were created using bootstrap official docs - https://getbootstrap.com/docs/5.1/getting-started/introduction/

Images used in this project were taken from unsplash and pexels - credit and thanks to all creators whos creative talent helped me create this project.

https://unsplash.com/
https://www.pexels.com/