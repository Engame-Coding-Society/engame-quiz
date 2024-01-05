#!/bin/bash

python3.11 -m venv venv

venv_path=""

if [ $# -ge 0 ]
then
  if [ "$1" = "local" ]
  then
    venv_path="venv/bin/activate"
  elif [ "$1" = "actions" ]
  then
    venv_path="/github/workspace/server/venv/bin/activate"
  fi
fi

source "$venv_path" && python3.11 -m pip install -r requirements.txt
