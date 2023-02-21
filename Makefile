.ONESHELL:
.SHELL := /bin/bash
.PHONY: ALL
.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

pre-commit-install: ## Install pre-commit into your git hooks. After that pre-commit will now run on every commit
	pre-commit install

pre-commit-all: ## Manually run all pre-commit hooks on a repository (all files)
	pre-commit run --all-files

docker-run: ## Starts app localy using docker-compose
	docker-compose up -d

docker-cleanup: ## Delete app deployed by docker-compose
	docker-compose down --rmi all -v

skaffold-dev: ## Build, tag and deploy artifacts via Helm chart using skaffold.yaml, make port-forward to containers and write logs of containers to stdout
	skaffold dev --port-forward=services

skaffold-run: ## Build, tag and deploy artifacts via Helm chart using skaffold.yaml
	skaffold run

skaffold-cleanup: ## Delete app deployed by skaffold
	skaffold delete

helm-add-jakuboskera-repo: ## Add jakuboskera Helm Charts repository, throw error if exist
	helm repo add jakuboskera https://jakuboskera.github.io/charts && \

helm-install: ## Deploy Helm release "my-guestbook" into Kubernetes using Helm chart "jakuboskera/guestbook" from Helm repository https://jakuboskera.github.io/charts
	helm install my-guestbook jakuboskera/guestbook

helm-cleanup: ## Delete Helm relaese "my-guestbook" from Kubernetes
	helm uninstall my-guestbook

# New targets here
