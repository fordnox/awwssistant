#!make

# Make sure you have .env file in root directory
include .env
export

# default target, when make executed without arguments
all: install lint

install:
	poetry lock
	poetry install --with dev

run:
	poetry run python -m awwsistant

agent:
	poetry run python -m swarmistant

lint:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest tests -k test_assistant --log-cli-level info --disable-warnings

t:
	poetry run pytest tests -s -k test_functions --log-cli-level info --disable-warnings

clean:
	rm -rf .pytest_cache
	find . -type f -name '*.pyc' -delete

.PHONY: all install run lint test t clean
