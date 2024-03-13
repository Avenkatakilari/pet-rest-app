# pet-rest-app
This is a demo project to show how to build a microservice with Django Restframework (DRF)
This demo project requires for stand alone mode.
1. Python 3+
2. MySQL 8+

Table of contents:

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Install](#install)
- [Tests](#tests)
- [Docker](#docker)
- [License](#license)

<!-- /TOC -->

## Install

```sh
git clone https://github.com/Avenkatakilari/pet-rest-app.git
cd petsapp
# Create virtual environment
python -m venv env
# Activate virtual environment
./env/Scripts/activate
# Install dependencies
RUN pip install -r requirements.txt
# Run the Django server
python manage.py runserver



```

Then visit [http://localhost:4040/](http://localhost:9009/)
Change port to desired on using SERVER_PORT variable in .env
## Tests
## add-user
To create user use postman or similar tools

http://localhost:9009/api/register using POST method

{
    "username":"testuser",
    "email":"testuser@gmail.com",
    "password":"NDg1MmU1ZW"
}

## To get token

http://localhost:9009/api/token using POST method

{
    "username":"testuser",
    "password":"NDg1MmU1ZW"
}

## To create a pet type

http://localhost:9009/api/pet-type using POST method
{
  "name: "dogs"
  "description" : "All types of Dogs those can be domesticated"
}

pass the bearer token which you got it from the token api in the authentication header

## To create a pet 

http://localhost:9009/api/pet using POST method
{
    "name":"Sparrow",
    "description":"My pet cooper is a Poodle",
    "user": {
        "id":1
        
    },
    "pettype":{
        "id":1
    },
    "city":"Los Angeles",
    "state":"CA",
    "phone":"242424242424"

}

pass the bearer token which you got it from the token api in the authentication header

Refer /api/urls.py to execute List, View, Update APIs

## Docker

You can also use docker for development.

```sh
docker build -t kv/test-mongo:1.0 .
```
Start the services
 Before you start the service make sure create a directory data on directory above the express-mongo-jwt

 e.g.,
  ```sh
  sudo mkdir ../data
  sudo chmod 777 ../data
  ```

```sh
docker-compose up -d
 ```

View the logs

```sh
docker-compose logs -f
```


Note that we are overriding the environment variable set in `.env` file because we don't want our data erased by the tests.



