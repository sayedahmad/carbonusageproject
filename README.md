# REST Carbon Usage API
REST API that exposes CRUD functionality to a database that stores carbon usage data for customers.


## Tech
1. Django 3.2.8
2. Django Restframework 3.12.4
3. Django Restframework Simplejwt 3.12.4
4. Docker
 

## Installation

To run the Application perform the following commands: 

* clone the project with  `git clone https://github.com/ssahim/carbonusageproject.git`
* `cd carbonusageproject/` change directory to the application root directory.

* ` docker build -t cusage .` to build the docker container.
* ` docker run -d -p 8080:8000  -v src:/drf_src --name cusage cusage `  Run the docker container on port 8080
* `docker exec -it cusage /bin/bash` to login into the container and create superuser with the following commands 
*  `python manage.py createsuperuser` 
* `exit` type exit to exit from the container  terminal.
* `http://localhost:8080/api/` is the base URL. you can use endpoinst mentioned in the  [documentation](https://github.com/ssahim/carbonusageproject/wiki). 


with the above commands the REST API application should succesfully run. The API will be ready for use. for more information on how to use the AIP please refer to the [documentation](https://github.com/ssahim/carbonusageproject/wiki). 


