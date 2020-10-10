# Wishl
Wishlist management service developed with Python3.8/Django3/DRF

## Usage
##### Define envs
You need to define environment variables values in the **wishl.env** file.
```
POSTGRES_DB=database_name
POSTGRES_USER=database_user
POSTGRES_PASSWORD=user_password 
WISHL_DB_HOST=db
WISHL_DB_PORT=5432
WISHL_TEST_DB=test_database_name
```
>You can rename them to whatever you want, but don't forget to add them to Django by editing **wishl/settingy.py**
##### Setup and launch
For building Docker images you need to execute following command
```
docker-compose build
```
After that execute commands for database migration and creating Django superuser:
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```
Next, just start the containers:
```
docker-compose up
```

Go to **http://localhost:8000**
