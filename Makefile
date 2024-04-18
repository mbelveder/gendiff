install:
		poetry install

gendiff:
		poetry run gendiff

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-force-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

test:
		poetry run pytest

test-verbose:
		poetry run pytest -vv

pytest-cov:
		poetry run pytest --cov=gendiff

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

lint:
		poetry run flake8 gendiff

selfcheck:
		poetry check

check: selfcheck test lint

build: check
		poetry build