#!make

# Make sure you have .env file in root directory
include .env
export

# default target, when make executed without arguments
all: install run

install:
	poetry lock
	poetry install --with dev

run:
	poetry run python bot.py

test:
	poetry run pytest test.py -k test_assistant --log-cli-level info --disable-warnings

t:
	poetry run pytest test.py -s -k test_vision --log-cli-level info --disable-warnings

clean:
	rm -rf .pytest_cache
	find . -type f -name '*.pyc' -delete

.PHONY: all install run test clean
