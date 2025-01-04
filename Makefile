up:
	docker compose up -d

down:
	docker compose down

migrate:
	docker compose run --rm backend-comands alembic upgrade head


