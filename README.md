# Books_API

Simple API based on instruction.
Deployed here, as a docker image : https://calm-mesa-41326.herokuapp.com/api/

## API route

Endpoints based on instruction, with prefix /api
- /books/<id>
- /books/db (Method POST with body {'q' : 'war'}
- /books?{sorting functionalities based on instruction}

## Used technologies
- Django
- Django rest framework
- Docker
  
## Running app locally

At branch production the Books_API are stored with configuration for Heroku deployment.
If user want to run the Books_API locally on PC, should make change in file:
  Books_API/STX_Semerjyan/settings/__init__.py to replace commented line:
```
  # from .settings import *
  from .localdev import *
  ```
Next user should [create Docker image and run it](https://docs.docker.com/engine/reference/commandline/build/). 
