from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV to JSON Conversion") \
    .getOrCreate()

csv_path = 'hdfs://namenode:8020/datalake/staging/csv/data'

target_folder = 'hdfs://namenode:8020/datalake/clean/csv'

df = spark.read.option('header', 'true').csv(csv_path)

df.write.save(path=target_folder, format='json')

spark.stop()
