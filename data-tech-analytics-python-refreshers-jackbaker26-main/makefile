# Makefile

# Target for running the tests
test-python:
	@PYDEVD_DISABLE_FILE_VALIDATION=1 JUPYTER_PLATFORM_DIRS=1 poetry run pytest --capture=sys tests/python_test.py
test-numpy:
	@PYDEVD_DISABLE_FILE_VALIDATION=1 JUPYTER_PLATFORM_DIRS=1 poetry run pytest --capture=sys tests/numpy_test.py
test-extra:
	@PYDEVD_DISABLE_FILE_VALIDATION=1 JUPYTER_PLATFORM_DIRS=1 poetry run pytest --capture=sys tests/extra_credit_test.py
test:
	@PYDEVD_DISABLE_FILE_VALIDATION=1 JUPYTER_PLATFORM_DIRS=1 poetry run pytest --capture=sys

install:
	@if command -v poetry > /dev/null; then \
		echo "Poetry found, installing dependencies with poetry..."; \
		poetry install; \
	elif command -v pipenv > /dev/null; then \
		echo "Pipenv found, installing dependencies with pipenv..."; \
		pipenv install; \
	else \
		echo "Neither poetry nor pipenv found. Please install one of them."; \
		exit 1; \
	fi

.PHONY: test-python test-numpy test-extra test install
