
# Django To Do List

It is a simple To Do list app made using Django Framework


# How to Use

1. `Fork` this Repository
2. `Clone` the repository
3. In `Command Prompt` or `Terminal` run `python` and copy paste the below code and `run`
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
4. You will get a random digits as output. `Copy` the output
5. create file name `secret_settings.py inside project folder`
6. `paste` the output in `THE-OUPUT-HERE` and copy paste the below code inside `secret_settings.py`
```python
SECRET_KEY = 'THE-OUTPUT-HERE'
```
7. Run migrations in `CMD` from `To Do` Folder
```
python manage.py makemigrations
python manage.py migrate
```
For Mac and Linux
```
python3 manage.py makemigrations
python3 manage.py migrate
```
8. `Run the project`
```
python manage.py runserver
```
for Mac and Linux
```
python3 manage.py runserver
```


-----

# App Screenshot


![App Screenshot](https://raw.githubusercontent.com/shaheem-pp/Djang-ToDo/main/app/static/Screenshot/Screenshot%202022-02-13%20at%203.54.29%20PM.png)

