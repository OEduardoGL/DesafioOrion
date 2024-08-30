import csv
import json
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd
from io import StringIO
from pyspark.sql import Row

source_file = "hdfs://namenode:8020/datalake/staging/html/data/"
target_folder = "hdfs://namenode:8020/datalake/clean/"

builder = SparkSession.builder.appName("convertendo xml to json")
spark = builder.getOrCreate()
string = spark.read.text(source_file)
test = string.toJSON()

row = Row("val") 
sparkdf = test.map(row).toDF()
sparkdf.write.save(target_folder, format='json', mode='append')