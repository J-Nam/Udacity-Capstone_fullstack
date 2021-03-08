# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/api` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we use handle the postgresql database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from our frontend server.

## Database Setup

You will first need to reset postgresql database path to yours in `models.py`

With Postgres running, restore a database using migration file provided.

1. In psql terminal, run:

```bash
create database capstone;
```

2. From the api folder in terminal run:

```bash
flask db init
flask db migrate
flask upgrade
```

## Running the server

From within the `api` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application.

## API Reference

### Getting Started

- Base URL: The backend app is hosted at the default, `https://jamwithus.herokuapp.com/`. If you are running the app using the backend API locally, API app is hosted at `http://127.0.0.1:5000/`, which you need to set as a proxy in the frontend configuration.

### Authentication

The app enables RBAC(roles-based access control) and uses Auth0 for the authentication.

Here are two roles and its permissions:

- Institution: `get:institutions`, `get:musicians`, `get:sessions`, `post:institutions`, `post:sessions`, `delete:institutions`, `delete:sessions`, `patch:institutions`, `patch:sessions`
- Musician: `get:institutions`, `get:musicians`, `get:sessions`, `post:musicians`, `delete:musicians`, `patch:musicians`

Here are test accounts/passwords for each role:

- Insitution: instapi@email.com/password123!
- Musician: musicianapi@email.com/password123!

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 404,
    "message": "page not found"
}
```

The API will return three error types when requests fall:

- 404: Page Not found
- 422: Unprocessable Entity
- 500: Server Error

### Endpoints

#### GET '/api/verification/<string:registerType>/<string:email>'

- Returns registered status: success: true/false
- Request parameters: registerType(institution/musician), user email

#### GET '/api/sessions/<string:email>'

- Returns success value, a list of all sessions, user typecheck value
- Request parameters: user email
- sample:

```
{
  "success": True,
  "sessions": [...],
  "isInstitution": True
}
```

#### GET '/api/session/<int:session_id>'

- Returns success value, a dictionary of the requested session information
- Sample:

```
{
  "success": True,
  "session": {...}
}
```

#### GET '/api/institutions'

- Returns success value, a list of all institutions
- Sample:

```
{
  "success": True,
  "institutions": [...]
}
```

#### GET '/api/musicians'

- Returns success value, a list of all musicians
- Sample:

```
{
  "success": True,
  "musicians": [...]
}
```

#### POST '/api/sessions'

- Returns success value and a new session dictionary
- Sample:

```
{
  "success": True,
  "new_session": {...}
}
```

#### POST '/api/institutions'

- Returns success value, a new institution dictionary
- Sample

```
{
  "success": True,
  "new_institution": {...}
 }
```

#### POST '/api/musicians'

- Returns success value and a new musician dictionary
- Sample

```
{
  "success": True,
  "new_musician": {...}
 }
```

#### DELETE '/api/sessions/<int:session_id>'

- Returns success value
- Request parameters: session_id
- Sample:

```
{
  "success": true
}
```

#### PATCH '/api/sessions/<int:session_id>'

- Returns success value
- Sample:

```
{
  "success": True
}
```

## Testing

To run the tests, run:

```
drop database capstone_test
create database capstone_test
python test_app.py
```
