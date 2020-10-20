# django-poll-app
Basic poll application. For learning the framework's purposes

<b>Project creation's command:</b></br>
py -m django startproject <projectname>
</br>

<b>Python shell run</b></br>
py manage.py shell

<b>Start server:</b></br>
py manage.py runserver
</br>
py manage.py runserver 8080 (to pass along the port)
</br>
py manage.py runserver 0:8000 (listen on all available public IPs)
</br>
py manage.py makemigrations polls (By running makemigrations, you’re telling Django that you’ve made some changes to your models)
</br>
py manage.py sqlmigrate polls 0001 (The sqlmigrate command takes migration names and returns their SQL)
</br>
py manage.py check (check issues)
</br>
py manage.py migrate (takes all the migrations that haven’t been applied and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database)
</br>
Essentially these are the three steps to save changes in model:
    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.
</br>
<b>Testing</b></br>
manage.py test polls (looks for tests in the polls application).
</br>
setup_test_environment() ( installs a template renderer which will allow us to examine some additional attributes on responses such as response.context that otherwise wouldn’t be available. 
Note that this method does not setup a test database)