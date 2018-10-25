To create virtual envirnoment
	> virtualenv django_dev
	> source django_dev/bin/activate

In virtual Envirnoment,

- to copy the packages list to requirements.txt
	> pip freeze --local > requirements.txt


- to install the django package
 	> pip install django
- to check which version of django is installed
	> python -m django –version


- To create a project in django use the below command, this command creates a project named ‘blog_project’

	> django-admin startproject blog_project
- to run the server, cd into the project folder
	> python manage.py runserver
		this command gives the url where our website is running

- The admin page of the website is by default created and can be accessed at (this is specified in url.py file)
	> http://127.0.0.1:8000/admin

- In the same project, you can create multiple applications
	> python manage.py startapp blog
		This creates app called blog

- Different views are created for the blog application by adding new functions into the views.py
and subsequently updating the urls.py. Views always return HTTPresponse or exception


- Updating settings.py file INSTALLED_APPS
After the app called ‘blog’ is created, it has to added to settings.py file for it to be installed in the project. This helps Django know the app ‘blog’ is there and also the templates folder created is picked up automatically. (blog.apps.blogconfig)


-Rendering .html files from template folder

- Rendering posts/context from db or dictionary, which are accessible from .html files for displaying using jinja(templating engine)

- jinga if else statement
- template inheritance using base.html page to be used as extends in other .html files
- adding bootstrap template code from bootstrap website for basic padding
- adding main.css file, navigation bar, main.html snippets
-url reference for links on the base.html from urls.py instead of hardcoding and changing it in multiple locations


ADMIN PAGE
	> python manage.py migrate
	> python manage.py createsuperuser
		- user: djangostg
		- pass: testpass

- user: testuser
-pass: pass!@#$

DATABASE TABLES FOR APPLICATIONS

django ORM (object relation mapper)
sqlite

represent databases structure as classes called models
models.py file

after crearting database model

CH4 
Admin page 

This will migrate the basic tables required
	> python manage.py migrate
This will give us the option now to create new superuser
	> python manage.py createsuperuser
This should be used when a database_structure aka classes aka models are created in the models.py file
        > python manage.py makemigrations


In the localhost:8000/admin,
- now we will be able to add users, remove users



CH5 
Database and migrations

django ORM is used for interacting with the DB (ORM=object relation mapper)
we are using sqlite for now

- The database structure is created in the models.py file as classes which will be used to create DB tables 
- After creating database model, run the command for django to read them
        > python manage.py makemigrations
- After this runs this there will be files created in blog/migrations/ to this specific migration which will have the same create details as our table
- However, to view the sql DDL statement of this you can run 
	> python manage.py sqlmigrate <app_name> <number_of_migration_file>
- Now to create the tables in the last we need to run
	> python manage.py migrate

There is Django python shell which gives access to these models for us to query them line by line,
these are used in the code files for fetching data from DB

Dunder __str__ for detailed information display

Jinja date filter for displaying the information in customized fashion

Register models in admin.py app file for the models to show up in the admin panel 
updating the Post model data directly from admin panel



CH6 
User registration form
Adding new fields to the forms using form inheritence in forms.py 
forms.save() command to save the details to the DB

Formatting the registration forms automatically using crispy-forms package (used for showing the forms in crispy fashion)
pip install the package > add it to installed_apps in settings.py > now its is available to load into html page files as {% load crispy_forms_tags %}

CH7
User Authentication page (login and logout pages)




CH8
User profile and Picture

create model with dunder str for Profile > Run makemigrations cmd after pip installing pillow > Run migrate command for changes to take effect in Database > register this model in Users application admin.py
-Pillow is package required to work with images inside django

Creating a profile page to display all of the user information like the profile image, email and username

Django signals to automatically trigger the profile creation for new user sign ups on the blog instead of doing it from admin page.


CH9
Update User Profile


