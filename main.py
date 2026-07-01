from spark.spark_session import create_spark_session
from spark.reader import read_logs
from spark.parser import parse_logs
from spark.extractor import extract_fields
from spark.classifier import classify_events

from spark.analytics import (
    event_distribution,
    authentication_summary,
    top_user,
    top_process
)

spark = create_spark_session()

logs = read_logs(
    spark,
    "data/raw/auth.log"
)

parsed_logs = parse_logs(logs)
extracted_logs = extract_fields(parsed_logs)
classified_logs = classify_events(extracted_logs)

# -------------------------------
# Analytics
# -------------------------------

print("\n===== EVENT DISTRIBUTION =====")

event_distribution(
    classified_logs
).show(truncate=False)


print("\n===== AUTHENTICATION SUMMARY =====")

authentication_summary(
    classified_logs
).show(truncate=False)

print("\n===== TOP USERS =====")

top_user(
    classified_logs
).show(truncate=False)

print("\n===== TOP PROCESSES =====")

top_process(
    classified_logs
).show(truncate=False)

# -------------------------------
# Sample Classified Logs
# -------------------------------

classified_logs.select(
    "timestamp",
    "process",
    "username",
    "event_type",
    "severity",
    "auth_status"
).show(50, truncate=False)

spark.stop()