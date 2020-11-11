#!/bin/bash -e

 #start mongodb database on docker

docker-compose -d
 #load data and latest data (just always load data all over with latest if shoudl be a cheap operation)

#data lod should happen via parser.py
python3.8 ./oracle/parsers.py
