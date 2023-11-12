# resource sharing
This is the webapp for resource sharing.

## Steps for setting up
1. Download the latest Python version.
2. It is recommended to use a virtual environment. If you just have Python, you can use `python -m venv venv`. If you are using some other management tool (like pyenv, conda, etc.), please check the documentation for the same.
3. Setup the Django project by running the following commands
```shell
python manage.py makemigrations // To make migration files.
python manage.py migrate // To migrate to the database.
python manage.py runserver // To run the server.
```
4. The application should be visible on your browser at `http://localhost:8000`.
