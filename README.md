# DevGrid - Weather

chalange description:

```
Design and build a service that collects data from an Open Weather API and store it as
a JSON data.
```


## build and run
It's needed to have docker and docker compose installed.
The compose will run the backend and the postgreSQL database.
The code will work without a .env file, all environment variables are initiated at src/api/settings.py
```
docker-compose up --build
```
After run the compose comand, will be able to use the API, the documentation will be available at `localhost:5000/doc`

To run property it needs to run the endpoint '/api/add_user/{username}' first, this will create a new user in table user.
After creating a new user, just run a request at '/api/weather/' as a post method passing the user id at the body, like:
```
{
  "user_id": "1"
}
```

You can see the porcentage of request weather at /api/weather/{user_id} as a get method.


## Test
To the better efficiency, some utilities files was removed from test, more information at .coveragerc

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
coverage run -m unittest discover
coverage report
```

## Description

To handler the problem it was used a basic dijkstra method to calculate the minimum value to delivery, usining 2 times, first to calculate to get on checkpoint and later to go to the finish.
```
.
├── ...
├── src
│   ├── __init__.py
│   ├── __main__.py
│   └── api
│       ├── __init__.py
|       ├── app.py
|       ├── config.py
|       ├── settings.py
|       ├── extensions.py
|       └── project
|           └── __init__.py
|           ├── restx.py
|           ├── api
|           |    ├── __init__.py
|           |    ├── user.py
|           |    ├── weather.py
|           |    └── health.py
|           ├── bo
|           |    ├── __init__.py
|           |    └── weather.py
|           ├── constants
|           |    ├── __init__.py
|           |    ├── CodeHttp.py
|           |    └── Message.py
|           ├── exception
|           |    ├── __init__.py
|           |    ├── DivisionError.py
|           |    ├── ExceptionError.py
|           |    └── NotTreatmentError.py
|           ├── repository
|           |    ├── __init__.py
|           |    └── database.py
|           ├── schema
|           |    ├── __init__.py
|           |    ├── user.py
|           |    └── weather.py
|           └── utils
|                ├── __init__.py
|                ├── doc_swagger.py
|                ├── logger.py
|                ├── response.py
|                ├── vars.py
|                └── utils.py
└── ...
```

## License
For open source projects, say how it is licensed.

