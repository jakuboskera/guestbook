ARG CREATED
ARG VERSION
ARG VCS_REF

LABEL \
    org.opencontainers.image.title="guestbook" \
    org.opencontainers.image.description="Guestbook is a simple cloud-native web application which allows visitors to leave a public comment without creating a user account." \
    org.opencontainers.image.created=${CREATED} \
    org.opencontainers.image.source="https://github.com/jakuboskera/guestbook" \
    org.opencontainers.image.url="https://hub.docker.com/r/jakuboskera/guestbook/tags" \
    org.opencontainers.image.version=${VERSION} \
    org.opencontainers.image.revision=${VCS_REF} \
    org.opencontainers.image.authors="iam@jakuboskera.dev" \
    org.opencontainers.image.vendor="Jakub Oskera" \
    org.opencontainers.image.base.digest="sha256:e80214a705236091ee3821a7e512e80bd3337b50a95392a36b9a40b8fc0ea183" \
    org.opencontainers.image.base.name="docker.io/library/python:3.9.10-alpine3.15"

WORKDIR /app

# First, copy the requirements.txt only as it helps with caching
# Details: https://pythonspeed.com/articles/docker-caching-model/
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY app ./app
COPY migrations ./migrations
COPY main.py .

ENV FLASK_APP=main.py

RUN useradd -m guestbook
USER guestbook

EXPOSE 5000

ENTRYPOINT [ "./entrypoint.sh" ]
