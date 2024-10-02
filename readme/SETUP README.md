# Project Setup

#### Setup steps are for Linux (Mint) system.

## BACKEND

#### Python virtual environment

Create a virtual env (Python)

```sh
pip install virtualenv
```

Create a environment

```sh
virtualenv env
```

Activate the new python environment

```sh
source env/bin/activate
```

Confirm the new python environment

```sh
which python3
```

<br>

#### pip

Access pip packages

```sh
pip list
```

Upgrade pip

```sh
pip install --upgrade pip
```

Install required packages from requirements.txt

```sh
pip install -r requirements.txt
```

<br>

## Postgres setup

An alternative to sqlite provided by Django

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

To initiate a new project

```sh
npx create-next-app@latest
```

Install packages/modules

```sh
npm run i
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

```sh
create-expo-app mobile
```

Install packages/modules

```sh
npm run i
```

If it is required to run the project on the web use the following command.

```sh
npx expo install react-dom react-native-web @expo/webpack-config
```

Run the app on mobile and web.

```sh
npx expo start
```
