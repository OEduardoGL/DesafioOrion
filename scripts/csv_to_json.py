from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV to JSON Conversion") \
    .getOrCreate()

csv_path = 'hdfs://namenode:8020/datalake/staging/csv/'
target_folder = 'hdfs://namenode:8020/datalake/clean'

sparkdf = spark.read.option('header', 'true').option('delimiter', ';').csv(csv_path)
sparkdf.write.save(path=target_folder, format='json', mode="append")
spark.stop()
