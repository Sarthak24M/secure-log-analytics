from pyspark.sql import SparkSession


def read_logs(spark: SparkSession, file_path: str):
    """
    Reads Ubuntu authentication logs into a Spark DataFrame.
    """
    return spark.read.text(file_path)