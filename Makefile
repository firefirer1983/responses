.PHONY: docs
init:
	pip install -r requirements-dev.txt

test-readme:
	python setup.py check --restructuredtext --strict && ([ &&? -eq 0] && echo "README.rst ok") || echo "Invalid markup in README.rst!"

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
