.PHONY: setup deps local deploy-dev deploy-stage logs-dev logs-stage lint test export help
.DEFAULT_GOAL := help

setup:  ## Install dependencies
	poetry install

deps:  ## Update dependencies
	poetry update

local: lint  ## Run the service locally
	poetry run chalice local --stage local

deploy-dev:  ## Deploy the service to dev
	poetry run chalice deploy --stage dev

deploy-stage:  ## Deploy the service to stage
	poetry run chalice deploy --stage stage

logs-dev:  ## Show logs in dev
	poetry run chalice logs -f --stage dev

logs-stage:  ## Show logs in stage
	poetry run chalice logs -f --stage stage

lint:  ## Run black, isort, flake8
	poetry run black app.py chalicelib tests
	poetry run isort app.py chalicelib tests
	poetry run mypy app.py chalicelib tests

test:  ## Run unit tests
	poetry run pytest tests/test_app.py

export:  ## Export lock file to requirements.txt
	poetry export -f requirements.txt --output requirements.txt --without-hashes

help:  ## Print Make usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
