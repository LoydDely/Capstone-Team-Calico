#!/bin/bash
# Initialize MediaWiki database from SQL dump
# This runs once when the database container starts

set -e

# Wait for MySQL to be ready
while ! mysqladmin ping -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent; do
    echo 'waiting for mysql...'
    sleep 1
done

echo "MySQL is ready"

# Check if tables already exist
if mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" -e "SELECT 1 FROM page LIMIT 1;" &> /dev/null; then
    echo "Database already initialized, skipping restore"
else
    echo "Restoring database from SQL dump..."
    mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" < /docker-entrypoint-initdb.d/mediawiki.sql
    echo "Database restored successfully"
fi
