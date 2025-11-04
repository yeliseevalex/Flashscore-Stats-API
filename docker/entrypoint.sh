#!/bin/bash
set -e

# Проверка аргумента
if [ "$1" = "web" ]; then
    echo "Starting FastAPI server..."
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
elif [ "$1" = "scrapy" ]; then
    echo "Starting Scrapy spider..."
    cd src/scrapy_app
    scrapy crawl flashscore
else
    echo "Unknown command, use 'web' or 'scrapy'"
    exit 1
fi
