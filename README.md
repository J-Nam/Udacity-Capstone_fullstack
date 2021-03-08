# Full Stack Capstone Project

## Full Stack JamWithUs

There are lots of event happening nowadays. Jamwithus is where institutions which are planning to have one(e.g. a charity which wants to get a fund for local hospitals) and talented musicians who wants to jam with people but also do something to give back to community. Simply join us and list the events that you are having and let musicians know about it! This world is still full of heartful people who care about one another, and believe in sharing 😊

## Starting

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Run react frontend app locally and it will use flask API app deployed on Heroku for the backend.

## About the Stack

### Backend

The `./api` directory contains a completed Flask and SQLAlchemy server. By default, react app is connected to remote API('https://jamwithus.herokuapp.com/'). You will need to change the path for each `fetch()` method in order to use a local API. You can reference models.py for DB and SQLAlchemy setup.

See [`./api/`](./api/README.md) for more details.

### Frontend

The root directory contains a complete create-react-app frontend to consume the data from the Flask server deployed on Heroku.

### Available Scripts

In the project directory, you can run:

#### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.
