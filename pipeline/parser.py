from pyspark.sql.functions import (
    col,
    regexp_extract,
    regexp_replace
)

# Pattern:
# TIMESTAMP HOST PROCESS[PID]: MESSAGE
LOG_PATTERN = (
    r"^(\S+)\s+"          # Timestamp
    r"(\S+)\s+"           # Hostname
    r"([^\[:]+)"          # Process name
    r"(?:\[(\d+)\])?"     # Optional PID
    r":\s*(.*)$"          # Message
)


def parse_logs(df):
    """
    Parse raw Ubuntu authentication logs into structured columns.
    """

    parsed_df = (
        df
        .withColumn(
            "timestamp",
            regexp_extract(col("value"), LOG_PATTERN, 1)
        )
        .withColumn(
            "hostname",
            regexp_extract(col("value"), LOG_PATTERN, 2)
        )
        .withColumn(
            "process",
            regexp_extract(col("value"), LOG_PATTERN, 3)
        )
        .withColumn(
            "pid",
            regexp_extract(col("value"), LOG_PATTERN, 4)
        )
        .withColumn(
            "message",
            regexp_extract(col("value"), LOG_PATTERN, 5)
        )

        # -----------------------------
        # Normalize process names
        # -----------------------------

        # Remove leading "("
        .withColumn(
            "process",
            regexp_replace(col("process"), r"^\(", "")
        )

        # Remove trailing ")"
        .withColumn(
            "process",
            regexp_replace(col("process"), r"\)$", "")
        )

        # Remove trailing "]"
        .withColumn(
            "process",
            regexp_replace(col("process"), r"\]$", "")
        )
    )

    
    return parsed_df