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

#

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

## Trello Board:

I created a Trello Board to better organise and visualise the project requirements which i'll update as I work through them:

![Trello](/Images/Trello.png)
#

## Wireframe:

I created a Wireframe of the websites main pages using Figma:

![Wireframe](/Images/Wireframe.png)
#


## ERD:

I then created the ERD on Canva (it would appear Lucid is currently not working) for how I planned for the various entities to interact: 

![ERD](/Images/ERD.png)
#

## Build Process:

Having played around with the Wireframe and due to the nature of the site (effectively journalling / social media) I think it would be better suited to mobile first development or potentially mobile one. 
#

## Build Notes:

Readme created before initiating main and project apps.
Created database in pgadmin 4
(ISSUE 1)
Created migrationscreated urls file in main app
Created templates folder in main app
Created about/hemp html files.
Linked those in views.py and urls.py
Created base.html and linked materialisecss 
Extended base.html to html templates
Created static/css file and extended it to base template\
Created further files/folders (home, profile, stats) and again linked to urls/views.
CSS changed to move footer down and fix it to bottom.
Started on authentication/authorisation as this is what I’ve most enjoyed from previous projects.
User/regi folders created
Login and register.html files created in registration folder
Added bootstrap so I could use crispy forms
Using basic nav bar to test pages before then creating burger menu
Followed https://learndjango.com/tutorials/django-signup-tutorial 
CREATED SUPERUSER.

Login page working.
Working on sign up.
Sign up redirects to homepage.
Created all password resent html pages. However all these also redirect to the homepage.

ISSUE 2 created.
Resolved - block content to block body.

Reset password requires email address linked to account.
Email address isn’t included in basic sign up (SCREENSHOT) 
So decided to use crispy forms. 

https://pypi.org/project/crispy-bootstrap5/

Register replaced sign up.
Tested password reset email sent and link works however password reset complete is still Django admin template (SCREENSHOT)
When you submit email address for password reset email the page (http://127.0.0.1:8002/main_app/password_reset/done/) reads as if password has been resent (SCREENSHOT) as opposed to email with link to reset password having been sent.
Amended templates. 

Unable to delete sign up html page, or signup view/path? If not using why won’t things work if code deleted???

Nav options updated with authentication.
(SCREENSH0TS)

Creating user update - so delete, password update (without email sent) etc.

ISSUE 3
User detail page not recognised (BROWSER SCREENSHOT)
And (TERMINAL SCREENSHOT).
Error “NoReverseMatch at /
Reverse for 'detail' not found. 'detail' is not a valid view function or pattern name.”

ISSUE 3 resolved - amended paths.
User detail (or profile) view now working.
User delete working.
Change password still using old Django templates (SCREENSHOT)

Deleted profile.html and stats.html as these will be on detail.html

password_change_done updated to html template.
Struggling to update password_change.html.
Realised from https://jatin-95284.medium.com/django-customize-the-auth-app-templates-with-tabler-io-admin-template-95998b44d2fe that the correct template was password_change_form.html. Updated my page to form.html and it worked.

Now to implement crispy forms, flash messages and email client.
Follow guide for crispy forms: https://github.com/django-crispy-forms/crispy-bootstrap5

Implemented crispy forms however not working as I want.
Spent enough time trying to get them to work for one day and it is largely cosmetic (I plan to address the appearance of the site once the functionaility is complete) so moved onto flash messages.

I want flash messages for:
Succesful registration.
Deleting profile.
Password change.

Found multiple messages would stack on each other (screenshot) so tried messages.clear(request) but realised this was now obsolete.
message.delete() also now obsolete so had to use the below:

        all_messages = messages.get_messages(request)
        for message in all_messages:
            message.used = True

ISSUE 4
ISSUE 4 RESOLVED.

Now amending password_change_done.html to user/detail.html and adding fash message to user/detail.html to confirm password change.
password_change_done.html deleted.

Succesful registration - done.

Added print message that should appear upon succesful user delete however it doesn't appear in console. 
User delete however works as user is deleted in Django admin.

Deleting profile. - done.
Achieved with "SuccessMessageMixin" and then adding success_message to view:
success_message = "Your 3GT account has been deleted."

----------------------------------------------------------------

RETURNED FROM 2 WEEK HOLIDAY.

Need to work on Flash message for Password change; currently reverts to django admin page?
As previously noted:

"Now amending password_change_done.html to user/detail.html and adding fash message to user/detail.html to confirm password change.
password_change_done.html deleted"

password_reset_done.html could also be deleted and redirected to "/" with a flash message of password successfully changed.

recreated password_change_done.html and will forgo the flash message for the time being as struggling to get it to work.


One of the big aims of the project for me was to connect the email functionality with a server host; so any emails triggered for password reset etc will actually be sent to user's inboxes as opposed to saved into a 'sent_emails' folder in VS Code. This was one of my aims for Project3 (NutriC02) on General Assembly's course but I ran out of time.

password_reset_email.html file created.
Tested it and sent email with html template apears in 'sent emails' folder.
(SCREENSHOT)

Email settings added to settings.py.
secrets.json and .gitignore created.
Gmail account created and email password hidden.

error due to being unable to locate secrets.json:
FileNotFoundError: [Errno 2] No such file or directory: 'secrets.json'
double checked spelling of all occurences of secrets.json.
tried using absoulte path to secrets.json instead of relative but received same error.
moved secrets.json and .gitignore into 3GoodThings folder (which then contains main_app etc).

ISSUE 5
attempted password reset however received error of:
"SMTPAuthenticationError at /main_app/password_reset/" in browser.
IMAP allowed in gmail settings. 





#


## Current Issues:

5. When attempting to send a password reset email to a registered address I receive error: "SMTPAuthenticationError at /main_app/password_reset/" with Exception Value of: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials r5-20020adfdc85000000b002f985eee030sm3934022wrj.84 - gsmtp')

- Double checked password/address was correct for 3gtproject@gmail.com; then changed password for account and updated in VS Code.
- Double checked SMTP server and port number were correct.
- Online suggestion point to turning "Less secure app access" on in the associated Gmail account however this option is now obsolete. 


#

## Resolved Issues:

1. Database created in pgAdmin4 and updated in settings.py however it's failing to connect; password would appear to be incorrect:

FATAL:  password authentication failed for user "postgres"

- I have reset the master password in pgAdmin4; deleted and recreated the database and double checked the password I am entering connects the server in pgAdmin4. Despite the password being correct in settings.py I still receive the fatal error message.

SOLUTION:

- I followed the link in settings.py for databases https://docs.djangoproject.com/en/4.1/ref/settings/#databases and since I last linked a database in settings.py both a HOST and PORT are now required. I updated settings.py to match my postgres server and it now works.

#

2. Multiple pages (signup.html and all password_reset.html) incorrectly display/link to the home page.

SOLUTION:

- I changed the reset in "password_reset_done.html" and "password_reset_form.html" to "change"; as per the urls provided by the Django auth app. I also came to realise I had used {% block content %} on the html pages where as on base.html I had used {% block body %}. Updating the html pages to 'body' resolved the issue.

#

3. The User Detail page is not recognised and results in an error in browser:

"NoReverseMatch at /
Reverse for 'detail' not found. 'detail' is not a valid view function or pattern name." 

and an error message in terminal:

"django.urls.exceptions.NoReverseMatch: Reverse for 'detail' not found. 'detail' is not a valid view function or pattern name."

- My user detail path read 'user/<int:pk>' as opposed to 'user/<int:pk>/detail' so I updated it:

    path('user/<int:pk>/detail', views.UserDetail.as_view(), name='user_detail'),

SOLUTION:

- Double checked my paths, views etc and realiased the name in my paths didn't need to include 'user' so updated all user paths to the below:

    path('user/<int:pk>/detail', views.UserDetail.as_view(), name='detail'),
    path('user/<int:pk>/update', views.UserUpdate.as_view(), name='update'),
    path('user/<int:pk>/delete', views.UserDelete.as_view(), name='delete'),

#

4. Despite using correct log in credentials; when trying to log in I am met with error message of:

"Please enter a correct username and password. Note that both fields may be case-sensitive."

- Attempted to fix with dedicated log in view.
- Removed crispy forms from log in page.
- Removed flash messages from base.
- Removed unused from django.contrib.auth.models import User from urls.py.
- Ammended password change back to how it was previously.
- git logged back to previous commit; carried on coding. Commited again.
- Came to work the following day and had same issue with log in credentials.
- Going to Django admin after creating new user and no new user is saved in Django administration. So instead of issue with log in it would appear new registered users aren't being saved.

SOLUTION:
- Checked my register view and I must have accidently deleted "user = form.save()" from it. I created a couple of new users and managed to succesfully log in with them. I checked Django Admin and all had been saved.

#







