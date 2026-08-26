#!/usr/bin/env bash

gunicorn myapp.wsgi:application