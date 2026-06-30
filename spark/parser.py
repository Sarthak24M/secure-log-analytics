from pyspark.sql.functions import regexp_extract, col

# One regex to capture the main fields
LOG_PATTERN = (
    r"^(\S+)\s+"          # Timestamp
    r"(\S+)\s+"           # Hostname
    r"([^\[:]+)"          # Process name
    r"(?:\[(\d+)\])?"     # Optional PID
    r":\s*(.*)$"          # Message
)

def parse_logs(df):

    return (
        df
        .withColumn("timestamp", regexp_extract(col("value"), LOG_PATTERN, 1))
        .withColumn("hostname", regexp_extract(col("value"), LOG_PATTERN, 2))
        .withColumn("process", regexp_extract(col("value"), LOG_PATTERN, 3))
        .withColumn("pid", regexp_extract(col("value"), LOG_PATTERN, 4))
        .withColumn("message", regexp_extract(col("value"), LOG_PATTERN, 5))
    )