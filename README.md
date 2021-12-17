# Code Test for Platform Eng 1

We would like you to write a small trivial application in any language of your choosing that provides the following HTTP endpoints…

- `GET /` Returns plain-text “Hello world” and HTTP status code 200
- `GET /status/alive` Returns an empty body and HTTP status code 200
- `GET /status/ready`
  - If the app has been running for less than 10 seconds, returns JSON content {“ready”: false} and HTTP status code 500
  - If the app has been running at least 10 seconds, returns JSON content {“ready”: true} and HTTP status code 200

Include some aspect of DevOps/Platform work, which may include any of the following...

- Dockerize your application
- Use a SaaS service to perform some automated step (of your choosing) whenever you push to your code repository for this application. For example...
  - Travis-CI
  - CircleCI
  - DockerHub
  - Heroku

## To Finish
1. ~~Dockerize.~~
2. ~~Sort out CircleCI.~~
3. Let's get this in to EC2!

## What Is This?
A small app written in Python using Flask, pytest, and gunicorn. It serves three endpoints as outlined in the test requirements, and has basic error handling for unexpected URLs.

The app can be run directly with `python main.py`, but it's also set up to run in a Docker container. The repo is set up to run basic endpoint tests when attempting to merge branches.

## To Run Locally
1. Clone repo
2. `docker build -t platform .`
4. `docker run -p 8000:8000 -d --name platform platform`

## cURL All Endpoints
curl -v 127.0.0.1:8000/
curl -v 127.0.0.1:8000/status/alive
curl -v 127.0.0.1:8000/status/ready

## Issues
1. Early goof renaming master > main. First commits were to the main branch renamed "readme_and_basic_structure"
2. Repo name stopped being funny after ~10 minutes
3. I was troubleshooting a dependency issue with circleCI and had the actual tests commented out until 11:56am today