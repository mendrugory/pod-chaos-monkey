.PHONY: kind destroy unittest docker-build load-image helm-install

local-environment:
	./venv_creation.sh

kind:
	kind create cluster --config environments/kind/kind.yaml

destroy:
	kind delete cluster --name development


unittest:
	PYTHONPATH=./src ./venv/bin/python -m unittest discover .

docker-build:
	docker build -t pod-chaos-monkey:${TAG} .

load-image:
	kind load docker-image pod-chaos-monkey:${TAG} --name development

helm-install:
	helm upgrade -i --create-namespace -n chaos pod-chaos-monkey ./chart

