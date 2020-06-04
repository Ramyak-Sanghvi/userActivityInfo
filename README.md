# userActivityInfo
Django application with User and ActivityPeriod models, written a custom management command to populate the database with some dummy data, and designed an API to serve that data in the json format.

API hosted at https://useractivityinfo.herokuapp.com/members/

INSTALLATION

1) Download or clone this repository.

2) If downloaded, Unzip the compressed folder containing the application into a suitable directory of your choice.

3) Go to the downloaded or cloned folder and activate virtual environment:

Example for Windows : (I have my repository in "D:")

=> Type following commands in Command Prompt :

i) d:

ii) cd userActivityInfo

iii) .\Scripts\activate

4) Now go to projectworkspace folder which is in current directory to run our Django project.

=> Continue in Command Prompt where we left in step 3 :

iv) cd projectworkspace

v) python manage.py make migrations

vi) python manage.py migrate

vii) python manage.py runserver

5) Take the HTTP address from the line beginning with "Starting development server at...".Put that web address into a web browser of your choice and go to it. The URL you enter should look something like this: http://127.0.0.1:8000

6) You now have the Django application running.

7) There will be no homepage at http://127.0.0.1:8000 , so you will get "Page not found" (404) Error!

8) To access API , goto http://127.0.0.1:8000/members/
