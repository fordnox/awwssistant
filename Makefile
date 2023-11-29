#!make

# Make sure you have .env file in root directory
include .env
export

# define the name of the virtual environment directory
VENV := .venv
CMD_PYTHON = ./$(VENV)/bin/python3

# default target, when make executed without arguments
all: venv run

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip3 install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run:
	$(CMD_PYTHON) bot.py

test:
	./$(VENV)/bin/pytest test.py --log-cli-level info --disable-warnings

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run test clean