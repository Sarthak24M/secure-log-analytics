from spark.spark_session import create_spark_session
from spark.reader import read_logs
from spark.parser import parse_logs

spark = create_spark_session()

logs = read_logs(
    spark,
    "data/raw/auth.log"
)

parsed_logs = parse_logs(logs)

parsed_logs.select(
    "timestamp",
    "hostname",
    "process",
    "pid",
    "message"
).show(20, truncate=False)

spark.stop()