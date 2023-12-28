#! /usr/bin/env bash

set -xe

isort .

mypy --install-types --non-interactive fastapi_skeleton/

mypy fastapi_skeleton

black fastapi_skeleton --line-length 88

flake8 fastapi_skeleton

bandit -r fastapi_skeleton/
