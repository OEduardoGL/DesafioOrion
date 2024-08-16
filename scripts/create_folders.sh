#!/bin/bash

until hdfs dfs -ls /; do
  sleep 5
done

hdfs dfs -mkdir -p /datalake/raw
hdfs dfs -mkdir -p /datalake/staging/csv
hdfs dfs -mkdir -p /datalake/staging/xml
hdfs dfs -mkdir -p /datalake/staging/html
hdfs dfs -mkdir -p /datalake/staging/json
hdfs dfs -mkdir -p /datalake/clean

