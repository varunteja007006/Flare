# Django

### Folder structure

- backend/
  - backend/ []
  - feedback/
  - login/
  - media/
  - sentiment_analysis/
  - static
  - .env
  - manage.py
  - requirements.txt

### Migrate tables after updating the models

Usual way

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

Forcefully

```sh
python manage.py migrate --run-syncdb
```

###

### Django auth

You can extend the authentication to include much more features and endpoints

https://drf-social-oauth2.readthedocs.io/en/latest/integration.html

https://django-oauth-toolkit.readthedocs.io/en/latest/

###

### Django Cities_light

If Cities_light database is empty. Follow the below steps:

1. Rollback all migration for the app

```sh
./manage.py migrate cities_light zero
```

2. Re-apply migration again

```sh
./manage.py migrate
```

3. Finally do a force import.

```sh
./manage.py cities_light --force-import-all
```

### PostgreSQL setup for Django

To be implemented later in the project

[https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes]

[https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8]

<br>
<br>

## Docker setup for React-Django project

[https://www.honeybadger.io/blog/docker-django-react/]

<br>
<br>

### Django Restframework

Why serializer & restframework needed?
[https://www.youtube.com/watch?v=L9ha9WUwTtc&list=PLoDOHR9iCew44kZu3IswYvQoh8b4wZvCo&index=16]

### Django Restframework simple JWT for authentication

[https://www.youtube.com/watch?v=KLua_cYGLec]

### Django Heroku deployment

[https://www.youtube.com/watch?v=5d8AQFF0Ot0]

### Django Blogs

- [Blog on Django Roadmap](https://www.paulox.net/2024/01/19/my-django-roadmap-ideas/)

- [Article on Django Deployment](https://appliku.com/post/deploy-django-hetzner-cloud)

##
