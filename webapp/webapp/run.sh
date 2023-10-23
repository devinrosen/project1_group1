#!/bin/bash
# export DBNAME=${EEN_CLUSTER}_${EEN_PG_DBNAME}

# until PGCONNECT_TIMEOUT=5 PGPASSWORD=$EEN_PG_PASSWORD psql -h "$EEN_PG_HOST" -U "$EEN_PG_USER" -d "$EEN_PG_DBNAME" -c '\q'; do
#   >&2 echo "Postgres is unavailable - sleeping"
#   sleep 1
# done

python3 manage.py collectstatic --noinput
python3 manage.py migrate

python manage.py runserver 0.0.0.0:8000