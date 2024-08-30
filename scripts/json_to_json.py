import csv
import json
import os
import pyspark
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql import Row

source_file = "hdfs://namenode:8020/datalake/staging/html/"
target_folder = "hdfs://namenode:8020/datalake/clean/"

builder = SparkSession.builder.appName("json converting")
spark = builder.getOrCreate()
string = spark.read.text(source_file)
test = string.toJSON()

row = Row("val") 
sparkdf = test.map(row).toDF()
sparkdf.write.save(target_folder, format='json', mode='append')

