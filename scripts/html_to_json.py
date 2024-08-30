import csv
import json
import os
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd
from io import StringIO
from pyspark.sql import Row

source_file = "hdfs://namenode:8020/datalake/staging/html/"
target_folder = "hdfs://namenode:8020/datalake/clean/"

builder = SparkSession.builder.appName("convertendo html to json")
builder = builder.config("spark.sql.execution.arrow.pyspark.enabled", "true")
spark = builder.getOrCreate()
string = spark.read.text(source_file)
test = string.toJSON()

row = Row("val") 
sparkdf = test.map(row).toDF()
sparkdf.write.save(target_folder, format='json', mode='append')