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

## Requirements

    asgiref==3.7.2
    async-timeout==4.0.3
    backports.zoneinfo==0.2.1;python_version<"3.9"
    colorama==0.4.6
    coverage==7.4.3
    Django==4.2.10
    django-db-connection-pool==1.2.4
    django-pytest==0.2.0
    django-redis==5.4.0
    djangorestframework==3.14.0
    drf-yasg==1.21.7
    exceptiongroup==1.2.0
    flake8==7.0.0
    greenlet==3.0.3
    inflection==0.5.1
    iniconfig==2.0.0
    mccabe==0.7.0
    mysqlclient==2.2.4
    packaging==23.2
    pluggy==1.4.0
    pycodestyle==2.11.1
    pyflakes==3.2.0
    pytest==8.0.2
    pytz==2024.1
    PyYAML==6.0.1
    redis==5.0.2
    SQLAlchemy==2.0.28
    sqlparams==6.0.1
    sqlparse==0.4.4
    tomli==2.0.1
    typing_extensions==4.10.0
    tzdata==2024.1
    uritemplate==4.1.1

## Installation

        Clone the repository:
    
        bash
    
    git clone <repository_url>
    
    Install dependencies:
    
    bash
    
    pip install -r requirements.txt
    
    Set up MySQL database:
