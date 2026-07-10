# python-django-api

This repository follows CodingEntrepreneurs's course Build a Django REST API with the Django Rest Framework at https://www.youtube.com/watch?v=c708Nf0cHrs .

* [Requirements](#requirements)

* [Installation](#installation)

* [Usage](#usage)

* [Django Shell](#django-shell)

## Requirements

* [Tested using Python 3.13](https://www.python.org)

## Installation

```bash
pip install virtualenv && \
  virtualenv env && \
  source env/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```

## Usage

```bash
python manage.py runserver
# http://localhost:8000
```

## Django Shell

```bash
python manage.py shell
```
