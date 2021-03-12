install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --force --user dist/*.whl

lint:
	poetry run flake8 gendiff
