install:
	poetry install

brain-game:
	poetry run brain-game

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_game
