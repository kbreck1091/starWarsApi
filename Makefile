.PHONY: test coverage lint security docker ci

test:
	pytest

coverage:
	pytest --cov=app --cov-report=term-missing

lint:
	flake8 app

security:
	bandit -r app

docker:
	docker build -t starwarsapi-local .

ci:
	./.local-ci