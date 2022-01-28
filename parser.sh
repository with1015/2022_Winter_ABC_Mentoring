#!/bin/bash

TARGET=$1
RESULT=result.log

python3 crawler.py > $TARGET
sed -r 's/<[^>]+>//g' $TARGET > $RESULT
