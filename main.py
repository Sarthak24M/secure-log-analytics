from pipeline.spark_session import create_spark_session
from pipeline.reader import read_logs
from pipeline.parser import parse_logs
from pipeline.extractor import extract_fields
from pipeline.classifier import classify_events
from pipeline.analytics import (
    event_distribution,
    authentication_summary,
    top_user,
    top_process
)
from pipeline.detections import (
    high_severity_alerts,
    privileged_activity,
    password_change_alerts,
    authentication_failures,
    brute_force_detection,
    excessive_sudo_detection,
    root_activity_detection
)
from pipeline.engine import build_pipeline

spark, classified_logs = build_pipeline() 




# -------------------------------
#Security Detection
#--------------------------------



print("\n===== EXCESSIVE PRIVILEGED COMMANDS =====")

excessive_sudo_detection(
    classified_logs
).show(truncate=False)

print("\n===== HIGH SEVERITY ALERTS =====")

high_severity_alerts(
    classified_logs
).show(truncate=False)

print("\n===== PRIVILEGED ACTIVITY =====")

privileged_activity(
    classified_logs
).show(truncate=False)

print("\n===== PASSWORD CHANGE ALERTS =====")

password_change_alerts(
    classified_logs
).show(truncate=False)

print("\n===== AUTHENTICATION FAILURES =====")

authentication_failures(
    classified_logs
).show(truncate=False)

print("\n===== POSSIBLE BRUTE FORCE =====")

brute_force_detection(
    classified_logs
).show(truncate=False)

print("\n===== ROOT ACTIVITY =====")

root_activity_detection(
    classified_logs
).show(truncate=False)

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

# classified_logs.select(
#     "timestamp",
#     "process",
#     "username",
#     "event_type",
#     "severity",
#     "auth_status"
# ).show(50, truncate=False)

spark.stop()