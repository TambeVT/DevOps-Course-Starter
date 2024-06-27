# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
C
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Setting up trello integration

This app uses trello API for storing the todo items. You will need to set up 
# A trello account  with a trello board.
# And generate an API key and token

Once you have done this, you will need to update the '.env' file to include your trello  details.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

##Running the test suite
To run the tests for the codebase run the following command:
...
poetry run pytest
...
(please make sure you have run 'poetry install' beforehand to install 'pytest')
if instead you'd like to run your test vis Docker please run thr following:
 docker build --tag todo-app:test --target test .
 docker run todo'app:test
 ---

## Building and running the App via Docker
To build the container for local development, please run

`docker build --tag todo-app:test --target test .` 

To run the container for local development, please run

docker run --publish 8000:5000  -it --env-file .env --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev

For the production container, the build and run commands are:
---bash
docker build --tag todo-app:pro --target production .
docker run --publish 8000:5000  -it --env.file .env todo-app:prod
