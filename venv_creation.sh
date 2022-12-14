#!/usr/bin/env bash

if [[ -f "venv" ]]
then
    rm -rf venv
fi

virtualenv  -p /usr/bin/python3.10 venv
venv/bin/python -m pip install --upgrade pip
venv/bin/pip install -r requirements.txt
