#!/bin/bash
if [ -f "public/source.zip" ]
then
  rm public/source.zip
fi

zip -r public/source.zip . -x server/**\* assets/**\* tests/**\* public/**\*
firebase deploy --only hosting
