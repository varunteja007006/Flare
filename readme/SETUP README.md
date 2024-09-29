# Project Setup

#### Setup steps are for Linux (Mint).

## BACKEND

### Python virtual environment

Create a virtual env (Python)

```sh
pip install virtualenv
```

Create a environment

```sh
virtualenv linux_env
```

Activate the new python environment

```sh
source linux_env/bin/activate
```

Confirm the new python environment

```sh
which python3
```

<br>

### pip

Access pip packages

```sh
pip list
```

Upgrade pip

```sh
pip install --upgrade pip
```

<br>

### Installing Django

```sh
python3 -m pip install Django
```

<br>

### Installing Django Rest Framework

```sh
pip install djangorestframework
```

Few configurations include, adding 'rest_framework' to your INSTALLED_APPS setting.
Checkout the [Django Rest Framework documentation](https://www.django-rest-framework.org/)

<br>

### Installing Django Cors Headers

```sh
pip install django-cors-headers
```

This helps to resolve the CORs errors when React frontend makes the request to the backend Django.
This also requires you to add the 'cors_headers' to your INSTALLED_APPS setting and also configuring
the middleware. Check it here https://pypi.org/project/django-cors-headers/ for more information.

<br>

## Postgres setup

#### Alternative to sqlite provided by Django

### Installing Postgresql and DBeaver

Download [Postgresql](https://www.postgresql.org/download/) and [DBeaver GUI](https://dbeaver.io/download/)

#### Setup the postgresql

[Postgresql guide by Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)

```sh
sudo systemctl start postgresql.service
```

Check the status

```sh
sudo systemctl status postgresql.service
```

Switch to postgresql account

```sh
sudo -i -u postgres
```

Access postgresql prompt

```sh
psql
```

Now the terminal shows `postgres=#`

Exit the postgresql prompt via

```sh
\q
```

Check the users in the table

```sh
SELECT * FROM pg_catalog.pg_user;
```

Create a new user if needed

```sh
CREATE USER newuser WITH PASSWORD 'my_password' SUPERUSER CREATEDB;

```

Grant permissions

```sh
GRANT CONNECT ON DATABASE your_database_name TO newuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN schema public TO newuser;
GRANT USAGE ON SCHEMA public TO newuser;
GRANT SELECT ON TABLE users TO newuser;

```

Now change the default password for postgresql

```sh
ALTER USER postgres PASSWORD 'mynewpassword';
```

<br>

#### Setup the DBeaver

Open the DBeaver GUI app.

1. In the top menu click `Database`.

2. Now choose `New Database connection` from the dropdown.

3. Choose `PostgreSQL` and click next.

4. Let fields be set with default parameters and give the new password in the password field.

5. Now run the `Test connection` to check for any errors.

Now you can create database --> table --> data.

<br>

## FRONTEND

Next JS setup:

```sh
npx create-next-app@latest
```

Run server

```sh
npm run dev
```

Run the production build

```sh
npm run build
```

Start the production build

```sh
npm run start
```

<br>

## ANDROID

We will use expo for the android app development. React Native CLI can also be used.
Expo out of the box provides better tools for building the android app.

First let us create a expo app & give it a name mobile.

```
create-expo-app mobile
```

If it is required to run the project on the web use the following command.

```
npx expo install react-dom react-native-web @expo/webpack-config
```

Run the app on mobile and web.

```
npx expo start
```
