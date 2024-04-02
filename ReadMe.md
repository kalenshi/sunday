## Sunday API Project with Redis and MySQL

## Description

    This project is a Djangorestframework-based API that utilizes Redis for caching and 
    MySQL as the database backend. It's designed to provide a robust foundation for 
    building scalable and efficient web applications with Django. 
    You are encouraged to clone the repository and make suggested changes/ improvements

## Features

    Django Framework: Utilizes Django, a high-level Python web framework, for rapid development and clean, pragmatic design.Redis Caching: Implements Redis for caching frequently accessed data, 
    improving API performance and reducing database load.MySQL Database: Integrates MySQL as the database backend, offering 
    reliability, scalability,and robust data storage capabilities.RESTful API: Builds a RESTful API following best practices, allowing for easy integration with 
    front-end applications and third-party services.Django Rest Framework (DRF): Utilizes DRF, a powerful toolkit for building Web APIs in Django, 
    providing serialization, authentication, and other essential features out of the box.Swagger Documentation: Generates API documentation 
    using Swagger, making it easy for developers to understand and interact with the API endpoints.Authentication and Authorization: 
    Implements authentication and authorization mechanisms to secure API endpoints and control access to resources.
    Testing: Includes comprehensive unit tests and integration tests to ensure the reliability and correctness of the API endpoints.
    Docker Support: Provides Docker configuration for easy deployment and scaling of the application in different environments.
     python -Xutf8 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 --database local > dump.json

## Installation

    `>> ### First time `
    1. git clone https://github.com/kalenshi/sunday.git
    2. navigate into the sunday project folder
    3. docker compose up --build
    4. docker compose exec app sh -c "python manage.py loaddata --format json dbDump.json"
    5. navigate to localhost:8000
    6. happy codding
    ## otherwise
    docker compose up 
    Side Note:
        If you encounter this Error `ModuleNotFoundError: No module named 'pkg_resources'
        Run pip install --upgrade setuptools


## Running tests
***
One of the ways to run unittests is to run the command 
> ` docker compose exec -it app bash -c "./run_test.sh"`
Another way is to execute to container with the app and run the following commands
> `docker container exec -it sunday-app /bin/bash`
Then run the command 
> `./run_test.sh`
From the command line
