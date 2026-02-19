#!/bin/bash
set -e

# Start MySQL normally first
/entrypoint.sh mysqld &
MYSQL_PID=$!

# Wait for MySQL to be ready
echo "Waiting for MySQL to start..."
while ! mysqladmin ping -h"127.0.0.1" -uroot -p"${MYSQL_ROOT_PASSWORD}" --silent 2>/dev/null; do
    sleep 1
done

echo "MySQL is ready"

# Check if the mediawiki database has tables
TABLE_COUNT=$(mysql -h127.0.0.1 -uroot -p"${MYSQL_ROOT_PASSWORD}" "${MYSQL_DATABASE}" -se "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='${MYSQL_DATABASE}';" 2>/dev/null || echo "0")

if [ "$TABLE_COUNT" -eq 0 ]; then
    echo "Database is empty, restoring from SQL dump..."
    if [ -f /docker-entrypoint-initdb.d/mediawiki.sql ]; then
        mysql -h127.0.0.1 -uroot -p"${MYSQL_ROOT_PASSWORD}" "${MYSQL_DATABASE}" < /docker-entrypoint-initdb.d/mediawiki.sql
        echo "Database restored successfully"
    else
        echo "ERROR: mediawiki.sql not found!"
    fi
else
    echo "Database already has $TABLE_COUNT tables, skipping restore"
fi

# Keep MySQL running
wait $MYSQL_PID
