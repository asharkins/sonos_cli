.PHONY: test

install:
	pip install -e .

lint:
	flake8 ./sonos 

lint-fix: 
	autopep8 --in-place --aggressive --recursive ./sonos
 
reqs:
	pip install -r requirements.txt
	pip install -r test/requirements.txt

env: 
	virtualenv venv

test:
	pytest test/test_sonos.py

denv:
	deactivate

pip:
	pip list