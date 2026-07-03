import time

from pipeline.engine import build_pipeline
from pipeline.analytics import (
    dashboard_summary,
    event_distribution,
    authentication_summary,
    top_user,
    top_process,
)

print("\n========== PIPELINE BENCHMARK ==========\n")

# ---------------------------------
# Build Pipeline
# ---------------------------------

start = time.perf_counter()

spark, classified_logs = build_pipeline()

end = time.perf_counter()

print(f"Pipeline Build Time : {end - start:.4f} seconds")


# ---------------------------------
# Dashboard Summary
# ---------------------------------

start = time.perf_counter()

dashboard_summary(classified_logs)

end = time.perf_counter()

print(f"Summary Time        : {end - start:.4f} seconds")


# ---------------------------------
# Analytics
# ---------------------------------

start = time.perf_counter()

event_distribution(classified_logs).collect()
authentication_summary(classified_logs).collect()
top_user(classified_logs).collect()
top_process(classified_logs).collect()

end = time.perf_counter()

print(f"Analytics Time      : {end - start:.4f} seconds")


# ---------------------------------
# Cleanup
# ---------------------------------

spark.stop()

print("\n========================================")