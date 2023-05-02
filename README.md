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

RESOLVED ISSUE 5.
(SCREENSHOT OF SUCCESFUL EMAIL TO MY GMAIL ACCOUNT)

--------------------------------------------------------------------------------

EMAIL ADDRESS VERIFICATION

However in resolving issue 5 I came to realise that I will only be able to send password reset emails to users if their email address is verified on AWS. 
I understand the actions I need to take to achieve this are as below:

"When a user signs up with their email address, you can trigger a verification email to be sent to that email address using the Amazon SES API or SDK. The email will contain a link or a code that the user can use to confirm that they own the email address.

To implement this process in your Django project, you can follow these general steps:

1. Configure Amazon SES for your Django project by adding your AWS access keys and configuring the email backend settings in your settings.py file.
2. When a user signs up with their email address, generate a verification code or link and store it in your database along with the user's email address.
3. Use the Amazon SES API or SDK to send a verification email to the user's email address. You can customize the email message and subject to include the verification code or link.
4. When the user clicks on the verification link or enters the verification code, verify the email address using the Amazon SES API or SDK. If the email address is verified, update your database to reflect the verification status.
5. When sending emails from your Django project, check that the "From" email address and the email addresses of any recipients have been verified before sending the email. You can use the AWS SES SDK to check the verification status of an email address."

However; after testing the password reset by email a number of times it would appear that 2 password reset emails are sent w

Email verification model created.
Updated my register view in views.py
Added send_verification_email to views.py
Tested registration. Recieved below error:

AttributeError at /register/
'Settings' object has no attribute 'BASE_URL'
Points to this line in views.py: "message = f'Hi, please click on the following link to verify your email address: {settings.BASE_URL}/verify-email/{verification_code}/'"

Updated settings with BASE_URL of local host port.
Attempted to register again and received the below error so registered email address is still not being verified on AWS's end:
"MessageRejected at /register/
An error occurred (MessageRejected) when calling the SendRawEmail operation: Email address is not verified. The following identities failed the check in region US-EAST-1:"

modified send_verification_email to use AWS SDK for Python (boto3) to send the verification email.

Received new error of "NoCredentialsError at /register/
Unable to locate credentials"

Explicitly passed my aws credentials to boto3.client() and now receive error message:
added "import json" to views.py and instructed to to read secrets the secrets:

with open('secrets.json') as f:
   secrets = json.load(f)


I now receive a new error of:

AttributeError at /register/
'dict' object has no attribute 'token_urlsafe'

verified in django admin users are being created and saved. 
print(secrets) statement is working as secrets are being printed to console so are being accessed in views.py
tried replacing the secrets.token_urlsafe with python's random:
verification_code = secrets.token_urlsafe(20)
verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
didnt resolve error so ammended back.

tried to uninstall and reinstall secrets but received error:
ImportError: Installing this module requires OpenSSL python bindings

downloaded and installed OpenSSL and imported to views.py.
uinstalled then reinstalled secrets.

still receiving 'dict' object has no attribute 'token_urlsafe' error so reverted back to verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=20)) and it worked - i received an email asking me to click on a line to verify my email address.
(SCREENSHOT OF SUCCESS MESSAGE FOR VERIFICATION EMAIL)

------------------------------------------------------------

EMAIL ADDRESS VERIFICATION

Clicking on the link in the email results in a 404 Page not found error:

Page not found (404)
Request Method:	GET
Request URL:	http://localhost:8000/verify-email/qPmuOToy6msv6J1qtFPe/

Created verify_email view and added path to urls.py.
Now get the following error when clicking the verify password link:

    FieldError at /verify-email/qPmuOToy6msv6J1qtFPe/
    Cannot resolve keyword 'email_verification_code' into field. Choices are: date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, user_permissions, username

Moved email_verfification_code from EmailVerification model to User model.
Changed user model to AbstractUser as opposed to built in Django user model. 
Attempted to makemigrations but received message:

    It is impossible to add a non-nullable field 'password' to user without specifying a default. This is because the database needs something to populate existing rows.
    Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit and manually define a default value in models.py.

Ran command "python3 manage.py makemigrations --empty main_app" to generate empty migration file. Populated file and made migrations which worked.
When I then attempted to runserver I received the below error:

    File "/usr/local/lib/python3.10/site-packages/django/db/migrations/graph.py", line 60, in raise_error
    raise NodeNotFoundError(self.error_message, self.key, origin=self.origin)
    django.db.migrations.exceptions.NodeNotFoundError: Migration main_app.0004_auto_20230501_0830 dependencies reference nonexistent parent node ('main_app', '0003')

Ran python3 manage.py showmigrations and there were no obvious issues. 
Deleted Migrations folder.
Created new Migrations folder and ran python3 manage.py makemigrations main_app.

Ran server and received below error:

    ProgrammingError at /verify-email/qPmuOToy6msv6J1qtFPe/
    column main_app_user.last_login does not exist
    LINE 1: SELECT "main_app_user"."id", "main_app_user"."last_login", "...

Updated user model to include last_login.
Unable to makemigrations automatically so created migration using python manage.py makemigrations main_app --empty.
Updated migration with "migrations.RunSQL('UPDATE main_app_user SET last_login = NOW() WHERE last_login IS NULL;')" and could then migrate.

After running server I now get error:

    ProgrammingError at /verify-email/qPmuOToy6msv6J1qtFPe/
    column main_app_user.is_superuser does not exist
    LINE 1: SELECT "main_app_user"."id", "main_app_user"."is_superuser",...
    
(issue is with line 135 of views.py)

the same error also effects requesting a password reset by email; it appears if I enter an email address and click 'send email'.


and when I attempt to register a new user I receive the below error:

    AttributeError at /register/
    Manager isn't available; 'auth.User' has been swapped for 'main_app.User'

(issue is with line 72 of view.py)

same error also effects login functionality. 




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

5. When attempting to send a password reset email to a registered address I receive error: "SMTPAuthenticationError at /main_app/password_reset/" with Exception Value of: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials r5-20020adfdc85000000b002f985eee030sm3934022wrj.84 - gsmtp')

- Double checked password/address was correct for 3gtproject@gmail.com; then changed password for account and updated in VS Code.
- Double checked SMTP server and port number were correct.
- IMAP updated to allowed in gmail settings. 
- Online suggestion point to turning "Less secure app access" on in the associated Gmail account however this option is now obsolete. 
- Suggestions to then create an "App password" in Gmail but again this would appear to be obsolete. 
- Amended EMAIL_BACKEND from 'django.core.mail.backends.smtp.EmailBackend' to 'django.core.mail.backends.console.EmailBackend' and 'sent' email now appears in the Terminal (SCREENSHOT)
- Decided to use AWS, signed up for account, created a user and added "AmazonSESFullAccess" permission to user. Generated access key and secret access key. Verified 3gtproject@gmail.com with AWS.
- Didn't realise that with AWS you can only send emails to addresses that have also been verified. Verfieid my personal email address; realised 3gtproject@gmail.com and my own email address were verified on "us-east-1" so amended "AWS_SES_REGION_NAME/ENDPOINT" to "us-east-1" as opposed to "us-east-2" and then I succesfully sent a password reset email from 3gtproject@gmail.com to my personal email address.

SOLUTION:
- Swapped from GMAIL to AWS and updated all necessary settings in settings.py. Verified the "DEFAULT_FROM_EMAIL" address on AWS.


