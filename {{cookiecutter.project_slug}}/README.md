# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Development Requirements

- Python3.10
- Pip
- Poetry (Python Package Manager)

### M.L Model Environment

```sh
$ MODEL_PATH={{cookiecutter.machine_learn_model_path}}
$ MODEL_NAME={{cookiecutter.machine_learn_model_name}}
```

### Update `/predict`

To update your machine learning model, add your `load` and `method` [change here](app/api/routes/predictor.py#L13) at `predictor.py`

## Run All Scripts

When you run the api for the first time, we recommend to run the following command.

```sh
$ make all
```

In this command, you can install and run all command.

## Installation

```sh
$ python -m venv venv
$ source venv/bin/activate
$ make install
```

## Runnning Localhost

```bash
$ make run
```

## Deploy app

```bash
$ make deploy
```

## Running Tests

```bash
$ make test
```

## Running Linter

```bash
$ make lint
```

The linter is [pysen](https://github.com/pfnet/pysen).

## Runnning Easter Egg

```bash
$ make easter
```

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

```bash
    app
    ├── api              - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for this application.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
    │
    tests                - pytest
```
