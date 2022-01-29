#!/bin/bash

TMP=temp.log
RESULT=$1

if [ -z $RESULT ]; then
  echo "Usage: source run.sh [FILE NAME.txt]"
  exit 1
fi

python3 crawler.py > crawl.log
echo "Crawling done. Start parsing..."

sed -r 's/<[^>]+>//g' crawl.log > $TMP

iconv -c -f utf-8 -t euc-kr $TMP > 0_$RESULT
rm $TMP
mv 0_$RESULT news_data
echo "Raw data parsining done. Start classification..."

python3 news_classification.py
