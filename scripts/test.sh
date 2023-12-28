#!/usr/bin/env bash

set -xe

pytest -vv --cov=fastapi_skeleton --cov=tests --cov-report=term-missing --cov-report=xml tests/ ${@}
