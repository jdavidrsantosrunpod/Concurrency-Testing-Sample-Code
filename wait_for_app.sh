#!/bin/bash
set -e

# URLs to check
APP1_URL="http://127.0.0.1:8000/health"

echo "Waiting for app ($APP1_URL) to be ready..."

# Loop until endpoints return 200
until curl -sf "$APP1_URL" > /dev/null; do
    sleep 2
done

echo "✅ app is ready. Starting handler..."
exec python handler.py
