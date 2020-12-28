# Asteria API

Asteria's API written in Flask. The data is stored in a Postgres database, and the API is
consumed by the iOS application.

## Install

Be sure to install the following dependencies before cloning the project.

* PostgreSQL (Version 13.1)
* Python (Version 3.9)

Create a database in the postgres CLI for the project with a custom user and password. Also, create the
database and name it `astoria_db`. Grant privileges to the custom user to the database.

The next step is to clone the project form the GitHub remote reposiory.

```
$ git clone ...
```

Once you have successfully cloned the repository, create a virtual environment and activate it.

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Install the dependencies defined in `requirements.txt`

```
$ pip install -r requirements.txt
```

Create a `.env` file at the root of the project. The file must have the following defined.

```
FLASK_APP=astoria
FLASK_ENV=development
DATABASE_URL=postgres+psycopg2://${username}:${password}@localhost:5432/asteria_db
SECRET_KEY=${random_secret_key}
```

Make sure to subtitue ${username} and ${password} with the user role created in the Postgres CLI.
Once you have that defined. Run the following to start the server.

```
$ flask run
```
