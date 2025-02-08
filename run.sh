#!/usr/bin/env bash

env

uvicorn src.main:app --host 0.0.0.0 --port 5000
