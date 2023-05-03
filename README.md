<div align="center">
    <h1>📘 Guestbook</h1>
    <a href="https://github.com/jakuboskera/guestbook/actions"><img alt="jakuboskera" src="https://img.shields.io/github/actions/workflow/status/jakuboskera/guestbook/release.yml?logo=github"></a>
    <a href="https://github.com/jakuboskera/guestbook/releases"><img alt="jakuboskera" src="https://img.shields.io/github/v/release/jakuboskera/guestbook?logo=docker"></a>
    <a href="https://hub.docker.com/repository/docker/jakuboskera/guestbook"><img alt="jakuboskera" src="https://img.shields.io/docker/pulls/jakuboskera/guestbook?logo=docker"></a>
    <a href="https://opensource.org/licenses/Apache-2.0"><img alt="jakuboskera" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"></a>
</div>

Guestbook is a simple cloud-native web application which allows visitors to
leave a public comment without creating a user account.

Application uses
[MVC architecture](https://www.giacomodebidda.com/posts/mvc-pattern-in-python-introduction-and-basicmodel/),
which is widely used software architectural pattern in GUI-based applications.

This application among other things, contains these endpoints:
- **API** (for interaction without UI) - [python-restx/flask-restx](https://github.com/python-restx/flask-restx),
- **Prometheus metrics** (for observability) - [rycus86/prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter),
- **Health** (health of a application) - [ateliedocodigo/py-healthcheck](https://github.com/ateliedocodigo/py-healthcheck).

Live demo of Guestbook application is deployed in
[Fly.io](http://fly.io) 🚀, **`public comments Welcome`**!🤗:

<p align="center">
    <b>https://guestbook.jakuboskera.dev</b>
</p>

## 📖 TOC

- [📖 TOC](#-toc)
- [🏁 Get started](#-get-started)
- [🛠 Used technologies](#-used-technologies)
- [🎉 Run in docker using docker-compose](#-run-in-docker-using-docker-compose)
    - [⚠️ Prerequisites](#️-prerequisites)
    - [🚀 Install](#-install)
    - [🧹 Cleanup](#-cleanup)
- [🎉 Run in Kubernetes](#-run-in-kubernetes)
    - [Using Helm](#using-helm)
        - [⚠️ Prerequisites](#️-prerequisites-1)
        - [🚀 Install](#-install-1)
        - [🧹 Cleanup](#-cleanup-1)
    - [Using skaffold and Helm](#using-skaffold-and-helm)
        - [⚠️ Prerequisites](#️-prerequisites-2)
        - [🚀 Install](#-install-2)
        - [🧹 Cleanup](#-cleanup-2)

## 🏁 Get started

1. Clone this repo

    ```bash
    git clone git@github.com:jakuboskera/guestbook.git
    ```

1. Navigate to a folder `guestbook`

    ```bash
    cd guestbook
    ```

1. Issue `make` command to see available targets, which you can use

    ```bash
    make
    ```

## 🛠 Used technologies

<div align="center">
    <img src="docs/used_technologies.png">
</div>

## 🎉 Run in docker using docker-compose

### ⚠️ Prerequisites
- docker-compose

### 🚀 Install

```bash
make docker-run
```

### 🧹 Cleanup

```bash
make docker-cleanup
```

## 🎉 Run in Kubernetes

Using Helm chart `guestbook` from Helm repository
<https://jakuboskera.github.io/charts>.

### Using Helm
#### ⚠️ Prerequisites
- Kubernetes 1.12+
- Helm 3.1.0+

#### 🚀 Install

```bash
make helm-install
```
#### 🧹 Cleanup

```bash
make helm-cleanup
```

### Using skaffold and Helm

Ideal for local Kubernetes development.

#### ⚠️ Prerequisites
- Kubernetes 1.12+
- Helm 3.1.0+
- skaffold

#### 🚀 Install

Build, tag and deploy artifacts via Helm chart using skaffold.yaml

```bash
make skaffold-run
```

Build, tag and deploy artifacts via Helm chart using skaffold.yaml,
make port-forward to containers and write logs of containers to stdout

```bash
make skaffold-dev
```

#### 🧹 Cleanup

```bash
make skaffold-cleanup
```
