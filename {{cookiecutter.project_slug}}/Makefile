SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

ifeq ($(TIMEOUT),)
TIMEOUT := 60
endif

ifeq ($(MODEL_PATH),)
MODEL_PATH := ./ml/model/
endif

ifeq ($(MODEL_NAME),)
MODEL_NAME := model.pkl
endif

export POETRY=poetry run
export PYSEN=${POETRY} pysen run
export PYTEST=${POETRY} pytest

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install up down easter

all: clean install test lint format up down easter

test:
	PYTHONPATH=app ${PYTEST} tests -vv --show-capture=all

lint:
	${PYSEN} lint

format:
	${PYSEN} format

install: generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry install

up: generate_dot_env
	docker-compose build
	docker-compose up -d
	@$(MAKE) easter

down:
	docker-compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

easter:
	./egg.sh

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
