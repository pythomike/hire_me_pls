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

## To Run Locally
1. Clone repo
2. `pip install -r requirements.txt`
3. `python main.py`

