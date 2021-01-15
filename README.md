# Pages & Pixels - Review & discuss your favourite books
[My deployed project is avaliable here](http://msp-3-pulp-pixels.herokuapp.com/get_index)

## What is the site?
A book review website where content is user generated. The website intends to be a community for book readers to be able to share 
their opinions on their favourite books by uploading reviews, as well as to allow users to discuss their favourite books by adding to review opinions 
through user comments. 

## What does the site aim to achieve?
The purpose of the website is to allow book lovers to express their thoughts on their favourite books, read other's thoughts on their favourite 
(or maybe not so favourite) books and to be able to take part in community discussion of these books via the user comments section
 on each review. 

Aditionally, the site is intended to earn the site owner money through purchase links to the book being reviewed.  

# UX

## User Stories
### First Time Visitor Goals

### Returning Visitor Goals

### Frequent User Goals

## Design
### Template
The site design uses a template from startbootstrap.com called [Modern Business](https://startbootstrap.com/previews/modern-business). The focus of this project was data centric development. I wanted to use a Bootstrap template 
to assist with some of the front end design so that I could spend more time focusing on the back end of the project. 

I chose to use this specific template for two main reasons: 
* It's very similar to startbootstrap's cleanblog template. But as the site relies on user generated reviews, 
I felt it was important to display multiple reviews per row so that as many users could see their own reviews on the home page as possible
(as opposed to the one per row most professionally written blog sites use - [example](https://www.tor.com/).
The Modern Business template allowed this with it's use of Bootstrap's card classes. 
* I wanted to use a carousel for my header so that it cycled through a welcome message, a search bar and a sign-up option - 
Later on in development, I decided against the carousel as it was taking too long to load and having the search bar on it meant it kept cycling to the next slide 
mid-search.   

The slight disadvantage of this template however, was that the layout was very tailored to business where I
wanted to project a sense of community through this site. As a result, I also made significant use of custom css and applied a number of bootstrap classes myself. 

### Images & colour
Images were taken from [Shutterstock](https://www.shutterstock.com/g/Tithi+Luadthong) (I've accidentally signed for a year's subscription, so I'm trying to get my use out of it)
The images played a big part in defining the look of the site - I picked three images that I wanted to convey a sense of imagination. 

These images are as follows: 
* [Image 1](static/img/head1.2.jpg)
* [Image 2](static/img/head2.jpg)
* [Image 3](static/img/head4.jpg)

These images then helped steer the design of the rest of the site as the colours used site wide were picked based on colours that complimented those of the images. 

(I also just really liked the images the user Tithi Luadthong had uploaded to Shutterstock)

### Logo
I wasn't too happy with the way the navbar brand title looked when it was just a text/link element. 
As a result I used [canva.com](https://www.canva.com/create/logos/) to make a basic free logo based on the colours I'd picked to use across the site. 

The logo is as folows: 

![Logo](/static/img/pplogo-crop.jpg)

This would also be useful as an alternate image if a user uploaded review didn't contain its own image. 

## Wireframes
Pdf's of my initial wireframes are linked below: 

* [Home Page](readme-assets/readme-wireframes/landing_page.pdf)
* [Read Review Page](readme-assets/readme-wireframes/read_review.pdf)
* [Sign up/Log in Page](readme-assets/readme-wireframes/signup.pdf)
    * Sign up & Log in page use same wireframe as layout is almost identical. 
* [Profile Page](readme-assets/readme-wireframes/profile.pdf)
* [Write Review/Edit Review Page](readme-assets/readme-wireframes/write_review.pdf)
    * Write Review & Edit Review page use same wireframe as layout is the same 
    (the only difference is edit page has prefilled form inputs). 

# Data
The project uses Python, Flask, MongoDB and Jinja in order to allow users to Create, Read, Write and Delete content from the website.

## Data Structure
The data in this project is stored in four collections in MongoDB:

### Reviews
![Reviews](/readme-assets/images/reviewsdb.jpg)
* Used for storing information that will be pulled from the database in review previews and full pages. 
* /write_review function in app.py adds this data into database. 
* Data is primarily accessed through use of jinja on HTML pages (e.g. book title - {{ review.book_title }})
* /edit_review function can ammend the details that have been saved into this collection.
* /delete_review removes this data from collection. 

### Users
![User](/readme-assets/images/userdb.jpg)
* Used to store user information.
* Username is stored in 'session' cookie to allow users to access pages that can only be accessed when logged in. 
* Username stored in 'session' is the username that will be stored in review collection by /write_review function when a user writes a review. 
This also applies to username displayed on comments posted on review.   
* 'session' cookie username also allows website to determine details to be shown on profile page & if user is able to access edit/delete options on review page. 
* Werkzeug used to encrypt password saved in db. 

### Comments
![Comments](/readme-assets/images/commentsdb.jpg)
* Used to store details of comments posted by user. 
* Comments uploaded by /comment function - works similar to /write_review function
* As mentioned in Users collection username stored in 'session' when uploading comment is saved as user_name in comments
* book_id in comments database matches the value of the _id for the review the comment was posted on - so site can determine which comments are to be displayed on which page.   

### Genres
![Genre](/readme-assets/images/genredb.jpg)
* This collection was initially going to have a bigger purpose accross the site. When writing reviews I wanted users to be given the opportunity to
either select from previously chosen genres OR to be able to add their own. 
* Ultimatley decided this overcomplicated things, and also made it possible for variations in genre names & spellings (e.g. if one user adds sci-fi & another user adds 'Science Fiction')
 to weaken search results. 
* As a result, I manually added all of the genres in the list.

# Features
## Existing Features
The key features of the site are as follows: 
* Responsive design across all device sizes 
* Navbar that displays options for site user based on whethr or not they are logged into the site. 
* Uses Python, Flask, MongoDB and jinja in order to display content sitewide that is drawn from a non-relational database.
* Landing page that allows users to: 
    * Browse previews of reviews uploaded to the site by other users
    * Search reviews uploaded to the site by other users. Searches can be based on four criteria - 
    Book Title, Author (of book), Genre & Username of review author.
    * Select a preview for a review that will then take them to a full review page based on the selected review's unique id in MongoDB
    * Log in to or sign up to the website
* Read Reviews page that allows users to:
    * Read reviews osted by other users.
    * Comment on reviews if logged in.  
    * If user is logged in and is viewing the page of a review they have written, they are given the option to edit or delete this review. 
    * An 'affiliate' link (a sort of example version, not actually affiliated with Amazon)- to an Amazon search page for the reviewed book.
* Sign up/Log in - Users can provide a Username, email address & password to sign up to the website. This allows them to add their own 
reviews to the site as well as to comment on other's reviews. Returning users can then log in with the details provided at sign up if they wish to access these features in future. 
* User Profile Page that allows users to: 
    * View reviews they have written (if logged in)
    * Edit or delete reviews they have written. 
* Write review page allows logged in users to submit their own reviews to the site. 
* Edit review page that allows logged in users to ammend previously submitted content. 

## Features left to implement
There are a number of features that I would have liked to include but that ultimatley weren't added because of time/feasabiity. 
These include:
* An option for users to edit and delete comments they have posted on the site. 
    * I hoped to include these two features, but based on time elected to focus on other higher priority features. 
* An option for users to visit other user's profile pages (Obviously without the ability to edit or delete that user's content)
    * Similar to above, due to time concerns I decided that I would have to leave this feature out - particulerly because it is 
    possible on the current version of the site to get all of this information using the search function on the site.
* User Profile pictures. 
    * I spent a long time trying to work out how to allow users to upload images when adding book reviews. I'd ended up speaking to Tutor support who advised against doing 
    this through Mongo directly and that my options would be to either do it via image url or to use an aditional service such as Cloudinary to store the images. 
    Ultimatley I chose to go the url route when it came to book covers because of time, but also with the logic that when it comes to book covers, 
    there will almost certainly be an image of the book cover that can be linked to. This approach however does not work as well with user profiles and 
    so I ended up dropping this feature. 


# Technologies Used
## Languages Used
* HTML
* CSS
* Python

## Additional technologies used
* [MongoDB](https://account.mongodb.com/account/login?signedOut=true)
    * Used to store data that is displayed across the site
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * Used for app.py code
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Used in combination with Flask to pull code from database and display it on website
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    * Used to encrypt passwords for user logins
* [Bootstrap](https://getbootstrap.com/)
    * Used to help with responsiveness and layouts
* [Start Bootstrap](https://startbootstrap.com/)
    * Provided Modern Business template used throughout
* [GitPod](https://gitpod.io/workspaces/)
    * Gitpod workspace used to build project
* [Github](https://github.com/)
    * Used to store code for project after beung pushed from GitPod
* [Heroku](https://www.heroku.com/)
    * Used to auto-deploy project based on latest version of project comitted to Github
* [canva.com](https://www.canva.com/create/logos/)
    * Used to design site logo

# Testing
## Testing User Stories
### First Time User Goals
1. As a first time user, I'd like to browse the site and read a review (I'm using reading on my phone on the bus).
    * 
    
2. As a first time user who has just finished reading a book, I'd like to post a review to share my opinion on it. 
    * On entering the site users on larger screens see a navbar that clearly provides the option to sign up to the site - 
    the first step in posting a review. 
    ![Navbar](/readme-assets/images/first-time-user/navbar.jpg)
    
    * In case this is not clear from the navbar, or if user is using a mobile device with a smaller screen (where navbar is hidden behing a navbar-toggler button)
    the home page on the site clearly states the purpose of the site and provides the option to 'Sign-up'.
    ![Header](/readme-assets/images/first-time-user/head.jpg)
    
    * Once user clicks the sign-up button, they are taken to a sign-up form. Here they are prompted to fill out their details 
    (and information on specific username format is given). 
    ![Signup](/readme-assets/images/first-time-user/signup.jpg)
    
    * Once a user submits the sign-up form they are redirected to their user profile. As they are a new user, this will state that they have not written any 
    reviews, but will prompt them to get started by offering the option to either write a review or browse reviews  
    ![Profile](/readme-assets/images/first-time-user/profile.jpg)

    * The user can then click the Write Review button and will be taken to the write review page where they can submit write and submit their review. 
    * Alternativley, if user decides they want to browse reviews before they commit to writing their own review, user can choose to browse. 
    If they do then decide to write a review, this option will be avaliable to them in the navbar as long as they are logged in.
    ![Navbar logged in](/readme-assets/images/first-time-user/navbar2.jpg)  


### Returning User Goals


### Regular User Goals
1. As someone who recently wrote a review for a book, I've thought about it some more and my thoughts have changed. I don't want to edit my review, I just want to get rid of it.
    * On entering the site


## Additional Testing
## Known Bugs
* 

# Deployment
My website has been deployed via Heroku. Heroku has been linked to my Github Repository for this project and auto deploys the code based on my latest commit. 
In order to deploy the project in this way I took the following steps: 

1. Created Github Repository
2. Created requirements.txt file & procfile in Gitpod workspace in order to tell Heroku what dependencies my project has. 
3. Logged in to Heroku & created a new app. 
4. Selected 'Deploy' in Heroku navbar. 
5. Chose 'Github' in deployment method. 
6. Searched for my project's Github repository in the repository search box. Selected correct repository. 
7. In same navbar I selected 'Deploy', selected 'Settings'. 
8. On this page selected 'Reveal Config Vars', this brings up fields to input key & value for config vars. 
9. Input the keys for IP, PORT, MONGO_DBNAME, MONGO_URI, and SECRET_KEY as well as corresponding values. 
10. Went back to 'Deploy', scorlled down to 'Enable Automatic Deployment' and clicked this. 
11. Heroku then built the application and provided a link to it. 

# Credits
## Code
* The [Modern Business](https://startbootstrap.com/previews/modern-business) template from startbootstrap.com was used to give the site it's layout. 
* startbootstrap.com's [Clean blog](https://startbootstrap.com/previews/clean-blog) was used to get the code for the header overlay. 
* [Bootstrap](https://getbootstrap.com/)'s library was used to help me make further changes to the layouts and provided code snippets for modals & buttons throughout. 
* [Code Institute](https://codeinstitute.net/) - a lot of the code used is based on CI tutorial videos. 
* Code Institute Slack channel - also useful for helping solve issues. 
    * One particular function that relies very heavily on this is my /comments function, which was based on a similar function I found someone posting about in there. 

* I relied a lot on Code Institute tutor support throughout the project, but particular areas I required particular help with were: 
    * Getting the review previews on the index page to link to a page based on the review's unique id. 
    * Linking comments to reviews by unique id.
    * Creating the {% if review_count  %} statement on the profile page.
    * I'd followed some Code institute tutorial videos a bit too closley early on and was loading Bootstrap through a file saved in my project rather than usin a CDN. Thsi was pointed out by a tutor. 
    * Learning how to link delete modal to unique id of review user wishes to delete. 
        * This last one actually had both me and the tutor supporting me stumped. We eventually found a solution on [pythonpedia](https://pythonpedia.com/en/knowledge-base/44606429/modal-window-in-jinja2-template--flask)
* Throughout the project I also regularly referred to the following:
    * [Stack Overflow](https://stackoverflow.com/) - provided a number of solutions to issues throughout the project.
    * [W3schools](https://www.w3schools.com/css/css3_images.asp)
    * [The Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
    * [Building a Blog App With Flask and Flask-SQLAlchemy by Pretty Printed](https://www.youtube.com/watch?v=XHGpPCYmPvI)
## Content
* All static content was written by me. 
* Review content is user submitted (but 90% of reviews on site at time of writing this were just added by me)

## Media 
* Static Images come from [Shutterstock user Tithi Luadthong](https://www.shutterstock.com/g/Tithi+Luadthong)  
* Logo designed using [canva.com](https://www.canva.com/create/logos/)

## Acknowledgements
* Code Institute Mentor Gerard McBride - for providing support throughout
* Code Institute Tutor Support - for also providing support throughout
* Websites used for design inspiration:
    * [Goodreads](https://www.goodreads.com/)
    * [Tor.com](https://www.tor.com/)
    * [Polygon](https://www.polygon.com/)
