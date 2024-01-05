#!/bin/bash

if [ $# -ge 0 ]
then
  if [ "$1" = "local" ]
  then
    python3.11 -m venv venv
    source venv/bin/activate
    pip3 install --upgrade pip
  elif [ "$1" = "actions" ]
  then
    source /github/workspace/server/venv/bin/activate
  fi
fi

python3.11 -m pip install -r requirements.txt
