install:
	python -m virtualenv .venv
	. ./venv/bin/activate
	pip install -r requirements.txt

run:
	. ./venv/bin/activate
	gunicorn --workers=2 src.app:app

tests:
	. ./venv/bin/activate
	unittest discover -s 'test' -p '*_test.py'
