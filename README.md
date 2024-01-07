# AirBnB clone - RESTful API
REST API is a software architectural style for Backend.

REST = “REpresentational State Transfer”. API = Application Programming Interface

Its purpose is to induce performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

REST API is Resource-based, a resource is an object and can be access by a URI. An object is “displayed”/transferred via a representation (typically JSON). HTTP methods will be actions on a resource.

### There are 6 constraints:
1. Uniform Interface
2. Stateless
3. Cacheable
4. Client-Server
5. Layered System
6. Code on Demand (optional)

## Table of Content
* [Environment](#environment)
* [Getting Started](#Getting Started)
* [Authors](#authors)

## Environment
Ubuntu 20.04 LTS using `python3` (version 3.4.3)

## Getting Started
You can launch the API with your storage type of choice and the correct environment variables.

* Database Storage `HBNB_MYSQL_USER=<mysqluser> HBNB_MYSQL_PWD=<mysqlpassword> HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=<mysqldb> HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app`

* File Storage `HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app`

## Authors
Isidro Bata - [Github](https://github.com/kiddingmz) / [Linkedin](https://www.linkedin.com/in/isidrobata)  
Jennifer Huang - [Github](https://github.com/feliciodeangela) / [Linkedin](https://www.linkedin.com/in/feliciodeangela)
