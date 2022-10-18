.PHONY: install format lint test sec

install:
	@poetry install

format:
	@black .
	@isort -m 3 .

lint:
	@black . --check
	@flake8 crypton_tool/
	@flake8 tests/
	@isort -m 3 . --check

test:
	@pytest -v
	
sec:
	@pip-audit