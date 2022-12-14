install:
	poetry install

brain-game:
	poetry run brain-game

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

make lint:
	poetry run flake8 brain_game
