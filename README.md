# Simple Django Project

## Requirements
- python 3.6

## How to install
```sh
git clone git@github.com:bcfurtado/simple-django-project.git && cd simple-django-project
mkvirtualenv simpledjangoproject -p $(which python3)
pip install -r requirements.txt
```

## How to run

### To run with populated data
```sh
make start-with-data
```

### To run with custom data
```sh
# Create an admin account:
make create-account
# Run the server
make migate start
# Login intro Admin:
http://localhost:8000/admin/
# You'll see the changes at:
http://localhost:8000/
```

## How to run the tests
```sh
make test
```
