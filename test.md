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

There is Django python shell which gives access to these models for us to query them line by line

