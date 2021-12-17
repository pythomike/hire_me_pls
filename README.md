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
2. Sort out CircleCI.
3. Let's get this in to EC2!

## To Run Locally
1. Clone repo
2. `docker build -t platform .`
3. `docker run -d -p 8000:8000 platform`

## cURL All Endpoints
curl -v 127.0.0.1:5000/
curl -v 127.0.0.1:5000/status/alive
curl -v 127.0.0.1:5000/status/ready

## Issues
1. Early goof renaming master > main. First commits were to the main branch renamed "readme_and_basic_structure"


## Things to Implement
1. Pylint Github Action (couldn't figure out how to eliminate some stlye checks - function docstrings)