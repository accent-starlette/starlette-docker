#! /usr/bin/env sh
set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-80}
LOG_LEVEL=${LOG_LEVEL:-info}

# Start Uvicorn with live reload
uvicorn --reload --reload-dir /app --host $HOST --port $PORT --log-level $LOG_LEVEL "$APP_MODULE"
