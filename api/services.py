from pipeline.cache import get_pipeline
from pipeline.analytics import event_distribution
from pipeline.detections import (
    authentication_failures,
    password_change_alerts,
    high_severity_alerts,
    privileged_activity,
)
from pipeline.analytics import (
    event_distribution,
    authentication_summary,
    top_user,
    top_process,
    dashboard_summary
)

from pipeline.detections import (
    high_severity_alerts,
    authentication_failures,
    password_change_alerts,
    brute_force_detection,
    root_activity_detection,
    excessive_sudo_detection
)


def dataframe_to_json(df):
    return [row.asDict() for row in df.collect()]


def get_summary():

    spark, classified_logs = get_pipeline()



    return dashboard_summary(classified_logs)

def get_analytics():

    spark, classified_logs = get_pipeline()

    analytics = {

        "event_distribution":
            dataframe_to_json(
                event_distribution(classified_logs)
            ),

        "authentication_summary":
            dataframe_to_json(
                authentication_summary(classified_logs)
            ),

        "top_users":
            dataframe_to_json(
                top_user(classified_logs)
            ),

        "top_processes":
            dataframe_to_json(
                top_process(classified_logs)
            )

    }

    

    return analytics

def get_detections():

    spark, classified_logs = get_pipeline()

    detections = {

        "high_severity_alerts":
            dataframe_to_json(
                high_severity_alerts(classified_logs)
            ),

        "authentication_failures":
            dataframe_to_json(
                authentication_failures(classified_logs)
            ),

        "password_changes":
            dataframe_to_json(
                password_change_alerts(classified_logs)
            ),

        "brute_force":
            dataframe_to_json(
                brute_force_detection(classified_logs)
            ),

        "root_activity":
            dataframe_to_json(
                root_activity_detection(classified_logs)
            ),

        "excessive_privileged_commands":
            dataframe_to_json(
                excessive_sudo_detection(classified_logs)
            )

    }

    

    return detections