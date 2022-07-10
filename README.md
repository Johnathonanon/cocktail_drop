# Cocktail Drop E-commerce Website

Cocktail Drop is a fully-functioning, interactive web application built using django, postgresql, bootstrap and deployed to heroku. People who participate in Precision Rifle Series can use the web application to trade and sell firearms. Precision Rifle Series is a rifle-based shooting sport that has championship style competitiors. Points can be collected from competitions and is a hobby enjoyed by people across the world. Of course, there are other competitive shooting sports that can also gain benefit from using the web application. Users can log-in, sign-up, post an advert and use contact information on an advert to commumicate with the seller. An agreenment can be made between the seller and buyer. Currently, web applications that fit into this category are few and far between. The web application is not limited to firearms, but scopes, accessories and ammunition can be traded as well. 



The live link can be found here - https://firearmexchange.herokuapp.com/

Initial brainstorming, planning and pitch of the web application: 

![Picture of planning diagram](static/readme_images/received_1181933939223231.webp) 

AmIResponsive snip

![Picture of AmIResponsive snip](static/readme_images/amiresponsive.png) 

## How to use the Web Application

The web application is used by users who wish to view adverts for firearm equipment, accessories, optics and ammunition. If the user wishes to post an advert to potentially sell or trade their item, they will need to create an account. This is done by clicking the "Register" button in the right hand corner of the header. Once done so, the user can log into their account and post an advert. Contact details should be inserted into the advert so that potential buyers can contact the seller. Once logged in, registered users can view their own adverts while also looking at adverts from other sellers. 

## Features

### Existing Features

- **User Walkthrough**

The user is greeted with the home page intially. The header contains the logo on the left hand side, which if clicked brings the user back to the homepage. On the right hand side of the header we have "Home", which if clicked brings the user to the homepage. Not every user will be aware that the logo could also bring them back to the homepage, ergo, the "Home" button was implemented. 
![Picture of Index Page - logged out](static/readme_images/indexpage1.png)
Next to the "Home" button is the "Register" button. If "Register" is clicked, the following page is displayed: 
![Picture of Sign Up Page](static/readme_images/SignUp.png)

Next to the "Register" button is the "Login" button when clicked looks like the image below:
![Picture of Login Page](static/readme_images/SignIn.png)

To create an account with Firearm Exchange, simply click "Register" and fill out the required information. See image below for guidance:
![Picture of Filling out Registration Details](static/readme_images/RegisteringInfo.png)

Once Registration information is filled in, click the green "Sign Up" button. Now that an account has been created, clicking the "Login" button and filling out the same information used to register the account will allow us to sign into the account. Once the screen looks like the image below, you are ready to sign in to the account by clicking the green "Sign In" button.

![Picture of Filling out Signing In Details to Login](static/readme_images/Signingintoaccount.png)

After logging into the account, the header will then look like the below image:
![Picture of Header after Logging In](static/readme_images/afterloggingin.png)

On the right hand side, the "Home" button is still present and will bring you to the homepage of the web application. Next to that is a drop down menu named "My F|E". If clicked this will display the following option:

![Picture of drop down menu](static/readme_images/dropdownmenu6.png)

If "My Advert" is clicked on, this will bring the web application user to the accounts list of posted adverts on Eirearm Exchange. Since this account does not have any listed adverts, this page is blank for now. 
![Picture of Blank My Adverts List](static/readme_images/myadvertsblank.png)
And with a populated list.
![Picture of Populated My Adverts List](static/readme_images/myadvertspopulated.png)

Next to the "My F|E" drop down menu is the "Logout" button. If clicked this will promptly log the user out of their account. This Button only appears if the user is logged into the web application. Next to the "Logout" button is the green "Post Advert" button. If clicked, it will bring the user to this page: 
![Picture of Blank Post Advert Page](static/readme_images/AdvertBlank.png)

If All of the information is filled out, the web application user can click "Post Advert". This will allow the user to post an advert about their item that they wish to sell or trade. See the image below as an example:
![Picture of Filled in Information Post Advert Page](static/readme_images/blasteradexample.png)

Once information is filled in to the users desire, the advert can be posted by clicking the green button "Post Advert".

Adverts are then used to populate the "Latest Adverts" list on the home page.
![Picture of Index Page - logged in](static/readme_images/indexpage2.png)


- **Back End**

  - The main data structure used in this application is the Advert Model. This is then used to populate a form, which in turn is rendered to the user via a view, and a template, and allows them to create an advert. The index page populates a list of all Advert objects in the databse sorting by most recently created. 

  - The My Adverts page allows users to view their own posted adverts with the option to edit or delete as required. Thus full CRUD functionality is implemented.


### Features Left to Implement

- A Search bar was orginally planned to be in the project. This would allow the user of the web application to search for desired adverts and find what they were looking for with ease. Time did not permit this feature to be fully implemented. 

- A messaging system was attempted to implement into the web application. The purpose was to allow user to user private interaction. This would allow communication between potential buyers and sellers. After much effort, tutoring support said the task would be too complicated and insinuated that it would be best to leave this feature on the back burner. 

- A tag system. Tags would appear at the bottom of an advert that a seller could decide on. If the advert was about an optics item, they could tag the bottom of the advert page with #opticalequipment and that would allow users who use similar words with the search function to ping the advert not only through words used, but also tags. 

- A commenting system on the advert. This was attempted, and followed the tutorial provided by the module but actually getting it to be fully working was just out of my grasp. I would be reminded by tutoring support that I should go to my mentor with this issue, but when doing so, my mentor would tell me to go to tutoring support. The full circle process would take hours. 

## Testing
The application has been consistently tested throughout its development by both myself and others. The gender and age of testers varied, with age ranging from 20s to 60s and testers having a diverse range of computer knowledge, and each tester found the application intuitive and easy to use.
 
Several bugs were found in development but all were corrected to the best of my knowledge at the submission of this project. 

The site had many issues during production but these were ultimately rectified thanks to help from tutor support, online resource, and avid troublshooting.

All code was passed throught the PEP8 linter and passing ok.

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

The live link can be found here - https://firearmexchange.herokuapp.com/

## Credits

I am grateful to the Code Institute tutors for their patient help with this project. Without them it would not have gone nearly so smoothly.

My mentor was very helpful and his knowledge and experience is highly appreciated.

Many elements of this project were created using bootstrap official docs - https://getbootstrap.com/docs/5.1/getting-started/introduction/
