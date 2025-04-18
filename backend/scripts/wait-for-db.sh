#!/bin/bash
set -e

until psql -h "db" -U "postgres" -d "mydb" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$@"