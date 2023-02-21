#!/bin/sh

set -e

flask db upgrade
gunicorn --bind 0.0.0.0:5000 -w 2 -t 2 --worker-class gthread --timeout 600 main:app
