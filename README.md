# DIY Blog Application for MDN Django Course
Clone this repo and go to the project forlder:
```
$ git clone https://github.com/savyukdima/blog.git
$ cd blog
```

Activate virtual environment and install all dependencies:
```
$ pipenv shell
$ pipenv sync
```
Make migrations, migrate database and create superuser:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```
Run project:
```
$ python manage.py runserver
```
