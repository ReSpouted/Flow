db_username = launcherapi
db_database = launcherapi

help:
	@grep -E '^\w+:.*?##\s.*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

shell:
	@docker compose exec app python manage.py shell

start: ## Start everthing, init if needed
	@-test ! -f .already-set-up && $(MAKE) init
	@docker compose up -d
	@touch .already-set-up

init: ## Start the project & load the initial database
	@mkdir -p storage/backend
	@docker compose down
	@docker compose up -d --build
	@$(MAKE) reset-db

reset-db: ## Reset the database
	@docker compose exec db dropdb -U${db_username} ${db_database} --force
	@docker compose exec db createdb -U${db_username} ${db_database}
	@$(MAKE) migrate
	@$(MAKE) fixtures

fixtures: ## Insert fixtures
	@docker compose exec app python manage.py loaddata minecraft project

migrations: ## Make migrations
	@docker compose exec app python manage.py makemigrations

migrate: ## Migrations
	@docker compose exec app python manage.py migrate
