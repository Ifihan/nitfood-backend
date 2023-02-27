up:
	@docker compose up

bash:
	@docker compose run web bash

build:
	@docker compose build

build-up:
	@docker compose up --build

createsuperuser:
	@docker compose run web python manage.py createsuperuser

down:
	@docker compose down --remove-orphans

flush-db:
	@docker compose run web python manage.py flush
	@make down

install:
	@pipenv install

makemigrations:
	@docker compose run web python manage.py makemigrations

migrate:
	@docker compose run web python manage.py migrate

shell:
	@docker compose run web python manage.py shell

test:
	@docker compose run web python manage.py test

up-d:
	@docker compose up -d