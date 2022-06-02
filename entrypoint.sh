#!/bin/sh

set -e

flask db upgrade
gunicorn --bind 0.0.0.0:$PORT -w 2 -t 2 --worker-class gthread --timeout 600 main:app
