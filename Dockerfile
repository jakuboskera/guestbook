# FROM python:3.9.7-alpine
FROM python:3.9.7-slim-buster

LABEL \
    org.label-schema.schema-version="1.0" \
    org.label-schema.name="guestbook" \
    org.label-schema.description="Guestbook is a simple cloud-native web application which allows visitors to leave a public comment without creating a user account." \
    org.label-schema.vcs-url="https://github.com/jakuboskera/guestbook" \
    org.label-schema.vendor="iam@jakuboskera.dev"

WORKDIR /app

COPY requirements.txt entrypoint.sh ./
RUN python3 -m pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY app ./

RUN useradd -m myuser
USER myuser

EXPOSE 5000

ENTRYPOINT [ "./entrypoint.sh" ]
