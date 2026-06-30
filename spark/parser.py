from pyspark.sql.functions import regexp_extract, col


def parse_logs(df):

    parsed = (
        df
        .withColumn(
            "timestamp",
            regexp_extract(col("value"), r"^(\S+)", 1)
        )
        .withColumn(
            "hostname",
            regexp_extract(col("value"), r"^\S+\s+(\S+)", 1)
        )
        .withColumn(
            "process",
            regexp_extract(col("value"), r"\s([^\s\[]+)(?:\[(\d+)\])?:", 1)
        )
        .withColumn(
            "pid",
            regexp_extract(col("value"), r"\[(\d+)\]", 1)
        )
        .withColumn(
            "message",
            regexp_extract(col("value"), r":\s(.*)$", 1)
        )
    )

    return parsed