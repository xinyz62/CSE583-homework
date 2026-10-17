#!/bin/bash
mkdir pronto
echo "This directory contains Pronto data." > pronto/README.txt
mkdir pronto/data
curl -o pronto/data/open_data_year_one.zip https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip pronto/data/open_data_year_one.zip -d pronto/data
head pronto/data/2015_trip_data.csv
