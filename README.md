# Flood Django

This is a very simple project. The structure of the project coppied from https://testdriven.io/blog/django-lets-encrypt/. 


## How to run

You can create your virtual environment and use the following comman, the project tested on python 3.10.

```
pip install -r .\requirements.txt
python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py runserver 8000
```

## Sample images

![alt text](https://raw.githubusercontent.com/NazaninTafreshi/flood_django/master/home.jpg)
![alt text](https://raw.githubusercontent.com/NazaninTafreshi/flood_django/master/station.jpg)
