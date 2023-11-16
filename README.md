# **Crypto Tracker Backend API**

**Developer: Christian Göran**

💻 [Live link](insert link to live API here)

This repository contains the API setup using Django REST Framework for the Crypto Tracker front-end application.

## Table of Contents

- [Project Structure](#project-structure)
  - [Code Structure](#code-structure)
- [User Stories](#user-stories)
- [Technologies Used](#technologies-used)
- [Agile Design](#agile-design)
- [Database Design](#database-design)
  - [Models](#models)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## Project Structure

The structure of this project is built to support a scalable and maintainable backend for cryptocurrency tracking. The project is organized into different Django apps, each serving a particular function within the larger application.

### Code Structure

The project's codebase is divided into various application folders to separate concerns and enhance modularity:

#### Project Apps

- **currency**: Manages cryptocurrency-related data and operations.
- **currencypost**: Handles user-generated content about cryptocurrencies.
- **favouritecurrencies**: Enables users to select and manage their favorite cryptocurrencies.
- **userprofile**: Manages user profile information and settings.

#### Core Django apps

- **settings.py**: Central configuration for the Django project, including middleware, installed apps, and database settings.
- **urls.py**: Route declarations for the project, directing HTTP requests to the appropriate view based on the URL.
- **wsgi.py**: Entry-point for WSGI-compatible web servers to serve the project.
- **models.py**: Definitions for the database schema and behavior of the application's data.

## User Stories

The application is built around user-centric stories that guide the development process to ensure the final product meets the actual needs of its users. Each epic contains several user stories, each with its own acceptance criteria.

(Insert User Stories and Acceptance Criteria here)

## Technologies Used

### Languages & Frameworks

- Python 3
- Django
- Django REST Framework

### Libraries & Tools

- [Django Cors Headers](https://pypi.org/project/django-cors-headers/) for handling Cross-Origin Resource Sharing (CORS).
- [Django Rest Framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for JWT-based authentication.
- [Gunicorn](https://gunicorn.org/) as a WSGI HTTP Server for UNIX.
- [Cloudinary](https://cloudinary.com/) for media storage solutions.
- [Psycopg2](https://www.psycopg.org/) as a PostgreSQL adapter for Python.
- [Pillow](https://pillow.readthedocs.io/en/stable/) for Python Imaging Library.
- Other libraries as listed in `requirements.txt`.

(Insert screenshot or text block of requirements.txt here)

### All libraries for deployment on Heroku

All dependencies required for deployment on Heroku are listed in the `requirements.txt` file.

(insert content of requirements.txt here)

## Agile Design

The development process followed agile methodologies, emphasizing incremental development and iterative progress through collaborative efforts.

### About the Agile Approach

- Adopted an iterative development process with regular sprints to introduce new features.
- Emphasized collaboration, flexibility, and customer feedback.

### User Stories

(Insert a brief overview of user stories or link to a detailed user stories document)

### Kanban Board

- Utilized a Kanban board to track progress and manage tasks efficiently.
- Organized tasks into categories: To Do, In Progress, and Done.

(Insert link to Kanban board or screenshots here)

### MoSCoW Prioritisation

- Applied the MoSCoW method to prioritize requirements based on their necessity.

(Insert a summary or visual representation of priorities here)

### Milestones

- Established clear milestones to mark significant stages of the project.

(Insert a list of milestones or link to a milestones tracking tool here)

### User Story Mapping

- Created a user story map to visualize the user journey and the scope of the project.

(Insert a user story mapping diagram or tool screenshot here)

### Sprint Reviews and Retrospectives

- Conducted sprint reviews and retrospectives to reflect on the work done and plan for improvements.

(Insert a brief overview or outcomes of recent sprints here)

### Continuous Feedback Loop

- Maintained a continuous feedback loop with stakeholders to ensure alignment with user needs and project goals.

(Insert examples of feedback implementation here)

By following these agile practices, the project ensured that the development process was adaptable to changes and aligned with the end-users' evolving needs.

## Database Design

The database schema was carefully designed to ensure efficient data storage and retrieval, providing a robust backbone for the application's functionality.

### Models and Relationships

- **Currency**: Represents cryptocurrencies with fields for id, name, symbol, current price, market cap, volume, and related data.
- **CurrencyPost**: Stores user posts related to specific cryptocurrencies.
- **FavouriteCurrencies**: Tracks user's favorite cryptocurrencies.
- **UserProfile**: Contains extended user information.

(Insert ERD or schema representation here)

## Features

The application is packed with features that provide users with a rich experience and necessary tools to interact with the platform effectively.

### Dynamic Pages and Interactivity

- Navigation menus for seamless site traversal.
- User authentication system with sign up and login capabilities.
- Personalized user dashboards and profile management.
- Cryptocurrency listings with the ability to "like" or "dislike" and maintain a list of favorites.

### Community Engagement

- Commenting system to foster user interaction.
- Admin capabilities for comment moderation.

(Insert screenshots or GIFs demonstrating features here)

## Validation

### Python Code

Python code was validated and formatted to adhere to PEP 8 standards, ensuring readability and maintainability.

(Insert validation results or links to validation tools here)

## Testing

Comprehensive testing was conducted to cover a wide array of scenarios, ensuring the application's reliability and stability.

(Insert link to TESTING.md or include details here)

## Deployment

### Heroku

The application was deployed to Heroku, following these steps:

- Set up config vars like CLOUDINARY_URL, DATABASE_URL, SECRET_KEY, etc.
- Added buildpacks for Python and Node.js.
- Configured automatic deployments from the GitHub repository.

(Insert deployment process details or screenshots here)

### Local Setup

For setting up the project locally:

- Clone the repository.
- Set up a virtual environment.
- Install dependencies from `requirements.txt`.
- Configure environment variables in `env.py`.

(Insert code block with commands for setting up the project)

## Credits

### Acknowledgments

- All contributors to the open-source libraries used in this project.
- The Django and Python community for their invaluable resources.
- [CoinMarketCap API](https://coinmarketcap.com/api/) for cryptocurrency data.

### Special Thanks

- To all beta testers and users providing feedback.
- To the development team for their relentless effort and dedication.

(Insert any additional credits or acknowledgments here)

## Thank You

A heartfelt thank you to everyone who has supported this project, from ideation to launch. Your contributions, feedback, and encouragement have been immensely valuable.

(Insert contact details or social links here)

## Bugs & problems

- Hitting the 32kb limit on Heroku config vars

  - When trying to add a config var with the coinmarketcap API, I am unable to, and the most probable cause for it is that I have reached the 32kb limit that Heroku has on config vars.
    - Solution: There seem to have been a corrupted Heroku app, after deleting and creating a new app, I could add the necessary config vars

- After deploying to Heroku, my currency model was empty and I need to find out how to make my Heroku app call the Coinmarketcap API to populate my currency model.

  - I added the Heroku Scheduler service to my Heroku app and configured it to run "python3 manage.py update_currencies" every 10 minutes.

- When sending a request from my signup form, a new user was registered to the database, but somewhere in the execution order after the registration I get a 500 error response. After looking through Heroku logs and not finding anything but a 500 error. I added LOGGING to my Django settings.py.
  - Solution: After 4-5 hours of searching for what the error could be. What eventually appeared to be the problem was the use of useNavigate/useHistory and that the use of this changed with the latest version of React. So after changing the code snippet "history.push("/signin");" and "const history = useNavigate();" to "const navigate = useNavigate();" and "navigate("/signin")" I managed to finally make it work.

LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'handlers': {
'console': {
'class': 'logging.StreamHandler',
},
},
'loggers': {
'django': {
'handlers': ['console'],
'level': 'DEBUG',
'propagate': True,
},
},
}

- The problem was then identified as being a missing Meta.model in my CurrentUserSerializer

- Having problems authenticating when sending requests from my frontend and I am not sure why my currentUser token is 'undefined'
  - All of this has been a cocktail of errors. The backend views.py for favouritecurrencies needed to be changed so only the specific authenticated user could retrieve his/her specific list of favourites. Then this array of favourites needed to be handled correcly in the frontend.
    (https://www.django-rest-framework.org/api-guide/permissions/)

###

Cloudinary storage
Rest
Pillow

Sources:

https://stackoverflow.com/questions/69510138/how-to-get-data-from-external-api-to-django-rest-framework - for connecting external API to Rest

https://medium.com/@chilinski.a/how-to-seed-a-django-api-with-data-from-an-external-api-b577b6e6ad54 - connecting external API to Rest

https://www.youtube.com/watch?v=QA6oTpMZp84 - using Coingeckos API

https://www.datacamp.com/tutorial/making-http-requests-in-python - Making a http request in Python

https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/ - custom management commands

https://www.youtube.com/watch?v=f3GfkvfpVAE - learning how to use coinmarketcaps api

https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide - how to use their api

https://www.django-rest-framework.org/api-guide/permissions/ - Learning more about authentication

https://www.freecodecamp.org/news/format-compact-numbers-with-javascript/ - format large numbers

---

# BlockBoard Backend API

<img src="/media/landingPage.png" ><br>

<hr>
Welcome to the backend of BlockBoard Crypto Tracker, a dynamic and robust web application designed to provide insights and analysis for cryptocurrency enthusiasts. This backend serves as the powerhouse of the application, handling data management, user authentication, and seamless integration with Coinmarketcap's cryptocurrency APIs.

Built using Django and Django REST framework, the backend infrastructure offers a secure, scalable, and efficient solution to manage vast amounts of data related to cryptocurrencies. The system is engineered to cater to both novice users and seasoned traders, providing them with up-to-date information and an interactive platform to track their favorite digital currencies.

This was my 5th and last project as part of Code Institutes course in Full Stack Software Development.

<hr>

## Table of contents

- [Overview](#overview)
- [UX](#ux)
  - [Strategy](#strategy)
  - [Scope](#scope-hr-)
  - [Structure](#structure-hr-)
  - [Skeleton](#skeleton-hr-)
  - [Surface](#surface-hr-)
    - [Color Scheme & Fonts](#color-scheme-and-fonts)
    - [Visual Effects](#visual-effects)
- [Agile Methodology](#agile-methodology)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Client bookints management](#client-bookings-management)
    - [Staff bookings management](#staff-bookings-management)
    - [Create bookings](#create-bookings)
    - [Menu](#menu)
    - [Information](#information)
  - [Potential Future Features](#pontential-future-features)
- [Responsive Layout and Design](#responsive-layout-and-design)
- [Tools Used](#tools-used)
  - [Python packages](#python-packages)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Deploy on heroku](#deploy-on-heroku)
  - [FORK THE REPOSITORY](#fork-the-repository)
  - [CLONE THE REPOSITORY](#clone-the-repository)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
- [Acknowledgements](#acknowledgements)

## Overview

This project serves as a comprehensive booking and management platform for the Dome Restaurant. The platform allows customers to easily reserve tables, add special notes for their bookings, and specify the number of guests. On the other side, staff members can manage these bookings efficiently through a staff-only interface. The system ensures that only available tables are offered to the customers, considering variables like time, date, and capacity. The platform is designed to handle real-world scenarios with ease. The application was built using Python (Django), HTML, CSS, and JavaScript, with data being stored in a PostgreSQL database and images on a Cloudinary account.

<br><br>
The deployed project can be accessed at [this link](https://dome-restaurant-hero-9071346b8ec2.herokuapp.com/).
<br><br>

## UX

This site was created according to the Five Planes Of Website Design:<br>

### Strategy<hr>

**User Stories:** <br>

| EPIC                  | ID  | User Story                                                                                                                                                       |
| :-------------------- | --- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Base Setup**        |     |                                                                                                                                                                  |
|                       | 1A  | As a developer, I need to create the base.html page and structure so that other pages can reuse the layout                                                       |
|                       | 1B  | As a developer, I need to create static resources so that images, css and javascript work on the website                                                         |
|                       | 1C  | As a site user I can see a navigation menu so that I can easily navigate through the site                                                                        |
|                       | 1D  | As a site user I can have a good UX/UI experience when browsing the site so that I am encouraged to stay on the website and eventually also visit the restaurant |
|                       | 1E  | As a developer, I need to set up the project so that it is ready for implementing the necessary features                                                         |
|                       | 1F  | As a developer, I need to create the footer for social media links and contact information                                                                       |
| **Stand Alone Pages** |     |                                                                                                                                                                  |
|                       | 2A  | As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist                                            |
|                       | 2B  | As a developer, I need to implement a 500 error page to alert users when an internal server error occurs                                                         |
|                       | 2C  | As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views                                             |
|                       | 2D  | As a restaurant owner, I would like a home page so that customers can view information on my restaurant                                                          |
| **Authentication**    |     |                                                                                                                                                                  |
|                       | 3A  | As a site user I can create an account so that I can create reservations in my name                                                                              |
|                       | 3B  | As a site user I can use my email and password to login so that my account is secure                                                                             |
|                       | 3C  | As a site user I can logout from my account so that I keep my account secure                                                                                     |
|                       | 3D  | As a site user I can reset my password by sending a link so that I can login even if I forgot my password                                                        |
| **Contact**           |     |                                                                                                                                                                  |
|                       | 4A  | As a user, I want to see the restaurant's opening and closing hours                                                                                              |
|                       | 4B  | As a user, I want to see location information on the website                                                                                                     |
|                       | 4C  | As a user, I want to see contact information on the website                                                                                                      |
|                       | 4D  | As a user, I want to see relevant information on the website                                                                                                     |
| **Menu**              |     |                                                                                                                                                                  |
|                       | 5A  | As a user, I want to see the restaurant's menu with details about ingredients and price, so that I can be completely aware of everything I want to order         |
|                       | 5B  | As a staff member I can update menu items so that I have an easier time managing dish items                                                                      |
| **Bookings**          |     |                                                                                                                                                                  |
|                       | 6A  | As a logged in user I can se a list of my reservations so that I can have a better overview                                                                      |
|                       | 6B  | As a logged-in staff member I can see upcoming reservations so that we can prepare the working day                                                               |
|                       | 6C  | As a logged-in staff member I can filter reservations so that I can see reservations for a specific date                                                         |
|                       | 6D  | As a logged-in user I can update a selected reservation so that choose a more convenient time                                                                    |
|                       | 6E  | As a logged-in staff member I can update a selected reservation to help clients                                                                                  | X   |
|                       | 6F  | As a logged-in user I can delete reservations so that I have control over my bookings                                                                            |
|                       | 6G  | As a logged-in staff member I can cancel bookings so that I can help a client with the cancellation                                                              |
|                       | 6H  | As a logged-in user I can select a time and date so that to finalize my reservation                                                                              |
|                       | 6I  | As a logged-in user I can see available tables for a specific date and time so that I can easier devide where to sit                                             |
|                       | 6J  | As a site user I get confirmation email when making a reservation so that the risk of becoming a no-show-reservation is minimized                                |
| **Deployment**        |     |                                                                                                                                                                  |
|                       | 7A  | As a developer, I need to remove comments, turn of DEBUG so that my project is ready for final deployment                                                        |
|                       | 7B  | As a developer, I need to deploy the project to heroku so that it is live for customers                                                                          |
| **Documentation**     |     |                                                                                                                                                                  |
|                       | 8A  | As a developer I need to write automated tests and testing documentation so that others and myself can better understand my project                              |
|                       | 8B  | As a developer I need to write readme.md so that others and myself can better understand my project                                                              |

**Project Goal:**<br>
The goal for the project is to create a website with good UX/UI in mind that is usefull to staff members and clients. The website should convey an emotional response in the user.

**Project Objectives:**<br>

- To create a simple and intuitive website that with the help of UX conveys an positive emotional response in the user;
- The design and content should help instill a better image of the client and their business;
- To make to clear categories of login accounts for staff members and clients;
- To implement features and design that upgrade the users experience;
- To make a responsive website that works on every device.<br><br>

### Scope<hr>

**Simple and Intuitive UX**<br>

- Create a website that follows the graphical profile and theme of the client;
- Create a header and a footer;
- Create a navbar that is visible throughout the website;
- Ensure that all user changes are notified to the user visually;
- Ensure that the user keeps their orientation during their navigation througout the website.

**Relevant Content**<br>

- Add relevant information about the restaurant, including its name, location, phone number and email;
- Create a clear and attrative presentation of the restaurant menu;
- Add photos that depict some of the food offered at the restaurant.

**Features for Upgraded Experience**<br>

- Create a reservation section that allows the users to see all the tables available for a specific date and time:
- Create a Menu feature that displays all the menu information;
- Create a Profile page for the user to see his upcoming bookings and favourite meals;
- Create a staff-member account to manage all the bookings for all the users;

**Clints % Staff Members Different Accounts**<br>

- Allow access to Profile page only for client type of users;
- Allow access to Manage Bookings page only for staff members type of users;
- Create a filter function only visible for staff-members for them to find specific reservations.

**Responsiveness**<br>

- Create a responsive website that works on every device and screen size.<br><br>

### Structure<hr>

The website is designed with a focus on user experience and is divided into 6 distinct pages, each serving a specific purpose. The content displayed on these pages varies based on whether the user is authenticated and whether they are a client or staff member. Here are the details:

- **Register/Login:** These pages allow users to create an account or authenticate into an existing one, providing access to various exclusive features.
- **Logout:** This is implemented as a modal dialog that allows users to securely log out of their accounts.
- **Home:** Accessible to all users, this page showcases the restaurant's ambiance, popular dishes, opening & closing times and contact info.
- **Menu:** This page displays the restaurant's menu items. An "Add to Favourite" feature is available only to logged-in clients.
- **Reservations/profile:** Exclusive to authenticated users, this page enables both clients and staff members to make or manage bookings.
- **Staff Manage Bookings:** Accessible only to staff members, this page displays all registered bookings, which can be grouped and filtered by date.

#### Flowchart

The project flowchart was created using <b>LucidChart</b>.<br><br>
[![N|Solid](static/images/flow_chart.png)](static/images/flow_chart.png)<br><br>

### Skeleton<hr>

**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed <details>

<summary>Here:</summary>
<img src="static/images/restaurant_wireframe.png"><br>
</details><br>

**Database**<br>
The project uses ElephantSQL as PostgreSQL relational database for storing the data.<br>
Two diagrams were created to represent the relationships between the tables. The first diagram was created before the website was developed, and it was used to identify the most relevant and useful attributes and tables. The final diagram was created after the website was developed, and it reflects the changes that were made to the attributes and tables.

<details>
  <summary>Initial Model</summary>
<img src="static/images/datamodel_plan.png" ><br>
</details>

<details>
  <summary>Final Model</summary>
<img src="static/images/datamodel.png"><br>
</details><br>

### Surface<hr>

#### Color Scheme and Fonts

- The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
- h1 - h6 elements: _Lato_
- paragraphs, links: _Baskerville_

<img src="static/images/font_color.png" width="60%"><br>

#### Visual Effects

- **Hover effects**<br>
<details>
  <summary>NavBar element hover and active effect</summary>
<img src="static/images/hover_effect.gif" width="40%"><br>
</details>
<details>
  <summary>Bootstrap standard button hover effect</summary>
<img src="static/images/buttonhover.gif" width="40%"><br>
</details>
<br>
<br>

## Agile Methodology

This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [GitHub](https://github.com/). As the user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress**, **Done** and **Not Implemented** lists.

<details>
<summary>Sprint Details</summary>

- **KANBAN BOARD**<br><br>
  <img src="static/images/kanban.png" width="60%"><br><br>
- **EPIC 1 - BASE SETUP**<br>
  -1A Create base.html<br>
  -1B Create static resources<br>
  -1C Create navigation menu<br>
  -1D Design according to good UX practices<br>
  -1E Setup Django project<br>
  -1F Create a footer<br><br>
  <img src="static/images/epic-1.png" width="60%"><br><br>
- **EPIC 2 - STAND ALONE PAGES**<br>
  -2A Implement 404 page<br>
  -2B Implement 505 page<br>
  -2C Implement 403 page<br>
  -2D Create a restaurant page<br><br>
  <img src="static/images/epic-2.png" width="60%"><br><br>
- **EPIC 3 - AUTENTHICATION**<br>
  -3A Implement the _Register_ page using the django-allauth module<br>
  -3B Implement the _Login_ page using django-allauth module<br>
  -3C Implement _Logout_ modal using django-allauth module<br>
  -3D Implement a _Reset password_ function<br><br>
  <img src="static/images/epic-3.png" width="60%"><br><br>
- **Sprint 4 - CONTACT**<br>
  -4A Implement opening & closing times on the webpage<br>
  -4B Implement information about location of the restaurant<br>
  -4C Implement contact information<br>
  -4D Implement other relevant information<br><br>
  <img src="static/images/epic-4.png" width="60%"><br><br>
- **Sprint 5 - MENU**<br>
  -5A Create a menu page with menu items<br>
  -5B Implement a function so that staff can enter new items on the menu<br><br>
  <img src="static/images/epic-5.png" width="60%"><br><br>
- **Sprint 6 - BOOKINGS**<br>
  -6A Implement reservation view for site user<br>
  -6B Implement reservation view for staff<br>
  -6C Implement reservation filter function for staff<br>
  -6D Implement function so site user can update a reservation<br>
  -6E Implement function so staff can update reservation<br>
  -6F Implement so user can delete a reservation<br>
  -6G Implement so staff can delete reservations<br>
  -6H Implement function so that user can create a reservation<br>
  -6I Implement so that site user can see available tables<br>
  -6J Implement so that user receives a confirmation email after creating a reservation<br><br>
  <img src="static/images/epic-6.png" width="60%"><br><br>
- **Sprint 7 - DEPLOYMENT**<br>
  -7A Prepare the project for deployment<br>
  -7B Deploy the project to Heroku<br><br>
  <img src="static/images/epic-7.png" width="60%"><br><br>
- **Sprint 8 - DOCUMENTATION**<br>
-8A Create automated tests<br>
-8B Write documentation for project in README.md<br><br>
<img src="static/images/epic-8.png" width="60%"><br><br>
</details><br><br>

## Features

### Existing Features and sub-pages<hr>

#### Client bookings management

Every client that is authenticated can access the _Reservation_ page where they have an overview over their reservations.

- From this view they can select to:
  _ Create a new reservation;<br>
  _ Edit an existing reservation;<br> \* Delete a reservation;<br>
  <br><br>

<img src="static/images/clientlist.png" width="30%"><br><br>

#### Staff bookings management

Staff users that are authenticated can access the _Reservation_ page where they have an overview of all the reservations made, as well as an additional feature of being able to search for reservations based on date or email-address.

- From this view they can select to:
  _ Create a new reservation;<br>
  _ Edit an existing reservation;<br>
  _ Delete a reservation;<br>
  _ Search for specific reservations<br>
  <br><br>

<img src="static/images/stafflist.png" width="30%"><br><br>

#### Create bookings

Every user that is authenticated can access the _Reservation_ page for making a reservation. This feature provides a form where the user can fill in the reservation details.

- The form is for selecting the date and time interval of the booking.
  The inputs are validated after the following rules:
  - The Date value should not be less than the current day;<br>
  - Entering Name, date and number of people is required;<br>
  - Maximum number of guests for a reservation is 8 people;<br>
  - The user can choose times from a list;
    - 1: 12:00 - 12:45
    - 2: 14:00 - 15:45
    - 3: 16:00 - 17:45
    - 4: 18:00 - 19:45
    - 5: 20:00 - 21:45<br><br>

<img src="static/images/create_reservation.png" width="30%"><br><br>

- If the reservation is submitted successfully, a success message will appear

#### Menu

The "Menu" section of our Django-based restaurant app allows users to easily browse through categorized dishes.

<img src="static/images/menu.png" width="30%"><br><br>

#### Information

The "Information" page serves as a one-stop destination for all essential details about the Dome Restaurant. It features our opening hours, contact information, and physical location.

<img src="static/images/information.png" width="30%"><br><br>

### Potential Future Features

- Add a feature where staff can add, remove and manage menu entries in the front-end interface.

- Email confirmation for users when a reservation is made, to decrease the risk of the reservation becoming a so called no-show.

- Password reset function where the user will get an email with a reset-password-link in case current password is forgotten.

## Responsive Layout and Design

The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, a custom breakpoint of max-width of 768px.

**Tested devices:**

    - iPhone 11
    - iPhone 13
    - iPhone 6/7/8
    - Ipad
    - Samsung Galaxy S8
    - MacBook pro 16'' M2

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[ElephantSQL](https://www.elephantsql.com/) - For PostgreSQL database<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[TinyPNG](https://tinypng.com/) - for compressing the images<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[Code Institute Pylint](https://pep8ci.herokuapp.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Firefox dev tools](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/open_the_inspector/index.html) - for debugging the project<br>
[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
Chrome LightHouse extension - for testing performance<br>

### Python packages

- Django (Framework)
- django-allauth (Library)
- django-bootstrap-datepicker-plus (Library)
- django-crispy-forms (Library)
- cloudinary (Library)
- gunicorn (Web Server)
- psycopg2 (Library)

## Testing

The testing documentation can be found at [TESTING.md](TESTING.md)

## Deployment

### Deploy on Heroku

1.  Create Pipfile

In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created.

2. Setting up Heroku

   - Go to the Heroku website (https://www.heroku.com/)
   - Login to Heroku and choose _Create App_
   - Click _New_ and _Create a new app_
   - Choose a name and select your location
   - Go to the _Resources_ tab
   - From the Resources list select _Heroku Postgres_
   - Navigate to the _Deploy_ tab
   - Click on _Connect to Github_ and search for your repository
   - Navigate to the _Settings_ tab
   - Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.

3. Deployment on Heroku

   - Go to the Deploy tab.
   - Choose the main branch for deploying and enable automatic deployment
   - Select manual deploy for building the App

### Fork the repository

For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:

- On [My Repository Page](https://github.com/christiangoran/dome-restaurant-repo), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository

For creating a clone of the repository on your local machine, use<b>Clone</b>:

- On [My Repository Page](https://github.com/christiangoran/dome-restaurant-repo), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits

### Content

Inspiration is taken from my own project in Indonesia - [Dome Lombok](https://www.dome-lombok.com)

### Media

All media used is created by myself.

### Code

- Further studies with [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
- Help with Bootstrap from their own excellent [documentation](https://getbootstrap.com)
- Database setup and much more with [Codemy.com](https://www.youtube.com/watch?v=A1nqCgAM6CE)
- Automated testing with [CodingEntrepeneurs](https://www.youtube.com/watch?v=5E_xLmQXOZg)
- Code from Gareth McGirr's [project](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak) used and customized for table verification
- A lot of time has been spent on re-watching Code Institutes splendid videos on Agile Methodologies, Django and Python to find solutions to problems.

## Acknowledgements

- Code Institute for providing a great course and support.<br>
- My mentor Gareth McGirr for great guidance and for wanting to help me more than expected of him with the problems encountered during the development of the project<br>
- Slack community for great involvement in helping each other<br>
