.PHONY: test

install:
	pip install -e .

lint:
	flake8 ./sonos ./test

lint-fix: 
	autopep8 --in-place --aggressive --recursive ./test
 
reqs:
	pip install -r requirements.txt
	pip install -r test/requirements.txt

env: 
	virtualenv venv

test:
	pytest  --cov=sonos test/test_sonos.py -v

denv:
	deactivate

pip:
	pip list