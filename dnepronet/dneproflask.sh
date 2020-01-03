#!/bin/bash -v

cd $(dirname $0)
FLASK_APP=dneproflask.py FLASK_ENV=development flask run
