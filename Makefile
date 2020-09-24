THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up start down destroy stop restart logs ps images migrate collectstatic
help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
build:
	docker-compose build $(c)
up:
	docker-compose up -d $(c)
start:
	docker-compose start $(c)
down:
	docker-compose down $(c)
destroy:
	docker-compose down -v $(c)
stop:
	docker-compose stop $(c)
restart:
	docker-compose stop $(c)
	docker-compose up -d $(c)
logs:
	docker-compose logs --tail=100 -f $(c)
ps:
	docker-compose ps
images:
	docker-compose images
migrate:
	docker-compose exec app python manage.py migrate
collectstatic:
	docker-compose exec app python manage.py collectstatic --clear
createsu:
	docker-compose exec app python manage.py createsu
