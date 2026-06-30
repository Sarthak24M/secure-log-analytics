from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Ubuntu Log Analysis") \
    .master("local[*]") \
    .getOrCreate()

logs = spark.read.text("system_logs.txt")

print("Number of log entries:", logs.count())

logs.show(20, truncate=False)

spark.stop()