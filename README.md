Just a template Django app with user registration and hopefully usable
docker-compose.

# Quick notes on getting around

Run containerized:

    ./compose/run dev up
    ./compose/run dev [down, or other docker-compose args...]

Create a local test env and run tests:

    python3 -m venv --prompt orchard .venv
    . .venv/bin/activate
    pip install -r requirements/test.txt
    pytest

Run dev locally, without postgres (creates db.sqlite3):

    ./manage.py migrate
    DJANGO_ALLOWED_HOSTS=127.0.0.1 ./manage.py runserver

Check or fix style:

    flake8 --exclude .venv --max-line-length 120
    black -l 120 file.py

# Credits

On the Django side this is basically cribbed from
[Cookiecutter](https://cookiecutter-django.readthedocs.io/) output. As
far as I can tell you are encouraged to modify and then license the
output yourself under one of the provided choices. I've added MIT here.
