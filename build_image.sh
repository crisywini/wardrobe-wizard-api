#!/usr/bin/env bash

if [ $# -eq 0 ]; then
  echo "Please specify the version tag, exiting..."
  exit 1
fi

echo "Now using tag version: $1"

VER=$1

docker-buildx build --platform linux/arm64 -t crisywini/wardrobe-wizard-api:$VER --push .
