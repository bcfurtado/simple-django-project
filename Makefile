create-account:
	python manage.py createsuperuser

start-with-data:
	python manage.py testserver fixtures.json

migrate:
	python manage.py migrate

start:
	python manage.py runserver

test:
	python manage.py test
