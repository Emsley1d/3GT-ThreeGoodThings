# 3GT - Three Good Things

## Description:

The	Three Good Things exercise is intended to increase happiness and a sense of	
wellbeing. An individual records 3 good things they've done on any given day; with the intention of redirecting attention and energy away from negative and towards positive thoughts. Studies have shown that people who wrote down and shared what they were grateful for each day, for just one week, ended up being happier up to six months later.

Mental health is one of the things I am passionate about and the Three Good Things exercise is something that has proved helpful to me in the past. 

# Planning:

## Initial Thoughts: 

- To allow users to sign up using different methods, email, Google etc.
- To provide email confirmation of sign up and option to reset password by email.
- Weekly and monthly calendar views of completed days; each day could be coloured differently. A completed day with 3 things logged could be green; a day with 0 things logged could be red.
- Social Media functionality; ability to have a 'feed' of other users; ability to follow other users and 'like' or support their posts in some way.
- Privacy button; so a users certain days/activities can be removed from their public feed. Or their profile can be made completely private. 
- Provide user's with alerts if they haven't done something for a while; i.e. not logged that they've been to the gym for a week.
- Table of a user's most popular things with drag/drop functionality so a user doesn't have to write the same things each day; they can just drag an item from their list and drop it onto a day to add it.
- Option to flip between light and dark modes.

## Project Aims:

- To incorporate as many of my initial thoughts as possible.
- To have full authentication and authoristation.
- Connect the email functionality with a server host.


## User Stories:

As a user I want to:

- Be able to sign up using different methods.
- Receive a confirmation email to confirm sign up.
- Be able to reset my password by email.
- Be able to delete my account.
- Add/remove up to 3 things per day.
- Categorise my things; i.e. physical activitiy, socialising.
- See a category breakdown of my things.
- Edit or delete paste entries. 
- See a weekly view of my things.
- See a monthly view of my things.
- Be able to follow other individuals.
- Be able to unfollow other individuals.
- Make certain days private from my followers or make my profile private.
- See a feed of my followers activities.
- 'Like' or 'Support' others posts in my feed.
- Receive 'Like' or 'Support' on my posts.
- See stats/a list of my most popular things.
- Be alerted if I haven't added anything for the current date.
- Be alerted if I haven't done one of my more popular/regular things for a week.

#

## Wireframe:

I created a Wireframe of the websites main pages using Figma:

![Wireframe](/Images/Wireframe.png)
#


## ERD:

I then created the ERD on Canva (it would appear Lucid is currently not working) for how I planned for the various entities to interact: 

![ERD](/Images/ERD.png)
#

# Build Process:

Having played around with the Wireframe and due to the nature of the site (effectively journalling / social media) I think it would be better suited to mobile first development or potentially mobile one. 
#

## Current Issues:

1. Database created in pgAdmin4 and updated in settings.py however it's failing to connect; password would appear to be incorrect:

FATAL:  password authentication failed for user "postgres"

- I have reset the master password in pgAdmin4; deleted and recreated the database and double checked the password I am entering connects the server in pgAdmin4. Despite the password being correct in settings.py I still receive the fatal error message.

SOLUTION:

- I followed the link in settings.py for databases https://docs.djangoproject.com/en/4.1/ref/settings/#databases and since I last linked a database in settings.py both a HOST and PORT are now required. I updated settings.py to match my postgres server and it now works.


