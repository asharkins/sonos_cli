install:
	pip3 install -e .

lint:
	flake8 ./sonos 

lint-fix: 
	autopep8 --in-place --aggressive --recursive ./sonos
 
reqs:
	pip3 install -r requirements.txt
	pip3 install -r requirements-test.txt

env: 
	virtualenv venv

denv:
	deactivate