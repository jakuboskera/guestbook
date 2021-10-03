#!/bin/sh

set -e

flask db upgrade
gunicorn --bind 0.0.0.0:$PORT -w 2 --threads 2 app:app
