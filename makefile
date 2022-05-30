install:
	poetry install

run:
	poetry run gunicorn --workers=2 src.main:app

tests:
	. ./venv/bin/activate
	unittest discover -s 'test' -p '*_test.py'

docker-build:
	docker build -t message-service:1.0 .

docker-run:
	docker run -p 4000:4000 message-service:1.0

kube-run:
	kubectl apply -f ops/deployment.yaml
	kubectl apply -f ops/service.yaml

kube-delete:
	kubectl delete -f ops/deployment.yaml
	kubectl delete -f ops/service.yaml