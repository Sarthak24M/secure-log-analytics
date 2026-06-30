from spark.spark_session import create_spark_session
from spark.reader import read_logs
from spark.parser import parse_logs
from spark.extractor import extract_fields

spark = create_spark_session()

logs = read_logs(
    spark,
    "data/raw/auth.log"
)

parsed_logs = parse_logs(logs)
extracted_logs = extract_fields(parsed_logs)

extracted_logs.select(
    "timestamp",
    "process",
    "username",
    "uid",
    "session_id",
    "target_user",
    "command",
    "auth_status",
    "message"
).show(40, truncate=False)

spark.stop()