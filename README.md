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
These images then helped steer the design of the rest of the site as the colours used site wide were picked based on colours that complimented those of the images. 

(I also just really liked the images the user Tithi Luadthong had uploaded to Shutterstock)

### Logo
I wasn't too happy with the way the navbar brand title looked when it was just a text/link element. 
As a result I used [canva.com](https://www.canva.com/create/logos/) to make a basic free logo based on the colours I'd picked to use across the site. 

The logo is as folows: 

![Logo] (/static/img/pplogo.jpg)



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


# Features

# Technologies Used

# Testing

# Deployment

# Credits



















<!--Found 'truncate' function here: https://stackoverflow.com/questions/33627646/python-flask-template-return-first-150-characters-->