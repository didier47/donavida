# DonaVida

Backend project for blood donors made with Django Rest Framework and MongoDB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

If you want to try, you will need these prerequisites

```
Python > 3.6
```

### Installing

First, clone the project on your computer

```
git clone https://github.com/didier47/donavida.git
```

then, create a virtual environment for the project, you can use virtualenvwrapper-win if your os is windows

```
pip install virtualenvwrapper-win
mkvirtualenv <name_you_desire>
```

after that, install the packages in requirements.txt to make sure you have everything needed

```
pip install -r requirements.txt
```

finally, set up mongoDB, you can easily do this using laragon if your os is windows, then, do the migrations

```
py manage.py migrate
```

now you can run it

```
py manage.py runserver
```

Navigate to localhost:8000/admin or localhost:8000/swagger and explore

Note: you will need user credentials, make sure to create an user with

```
py manage.py createuser
```

## Authors

* **Didier Gaona**

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details
