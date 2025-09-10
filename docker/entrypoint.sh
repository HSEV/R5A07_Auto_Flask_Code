#!/usr/bin/env sh
set -e

# Optional DB wait loop
if [ -n "$MYSQL_HOST" ]; then
  echo "Waiting for MySQL at ${MYSQL_HOST}:${MYSQL_PORT:-3306}..."
  for i in $(seq 1 60); do
    (nc -z "$MYSQL_HOST" "${MYSQL_PORT:-3306}" >/dev/null 2>&1 && echo OK && break) || true
    sleep 1
  done
fi

# Initialize database (idempotent)
if [ "$INIT_DB" = "1" ]; then
  echo "Running db_init.py..."
  python db_init.py || echo "db_init.py failed (continuing): $?"
fi

# Run Flask app
exec python app.py
