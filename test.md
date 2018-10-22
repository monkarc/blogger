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

Formatting the registration forms automatically using crispy-forms package
pip install the package > add it to installed_apps in settings.py > now its is available to load into html page files as {% load crispy_forms_tags %}


