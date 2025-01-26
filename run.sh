#!/usr/bin/env bash

env

uvicorn src.main:app --reload --port 5000
