FROM python:3.9.7-slim-buster

LABEL \
    org.label-schema.schema-version="1.0" \
    org.label-schema.name="guestbook" \
    org.label-schema.description="Guestbook is a simple cloud-native web application which allows visitors to leave a public comment without creating a user account." \
    org.label-schema.vcs-url="https://github.com/jakuboskera/guestbook" \
    org.label-schema.vendor="iam@jakuboskera.dev"

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
