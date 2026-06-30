from pyspark.sql import SparkSession


def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("SecureLogAnalytics")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark