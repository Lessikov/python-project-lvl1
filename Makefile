install:
	poetry install

brain-games:
	poetry run brain-games
	s
brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user ~/python-project-lvl1/python-project-lvl1/dist/hexlet_code-0.1.0-py3-none-any.whl
make lint:
	poetry run flake8 brain_games
make reinstall:
	python3 -m pip install --force-reinstall --user ~/python-project-lvl1/python-project-lvl1/dist/hexlet_code-0.1.0-py3-none-any.whl


 
