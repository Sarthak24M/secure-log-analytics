from pyspark.sql.functions import (
    col,
    when,
    lit
)

from .patterns import (
    AUTH_FAILURE,
    AUTH_SUCCESS,
    PASSWORD_CHANGE,
    PRIVILEGED_COMMAND,
    SESSION_OPEN,
    SESSION_CLOSE,
    CRON_JOB,
    SYSTEM_SHUTDOWN,
    SYSTEM_STARTUP
)


def classify_events(df):

    return (

        df

        # --------------------------------------------------
        # Event Type Classification
        # --------------------------------------------------

        .withColumn(

            "event_type",

            # Authentication Failures
            when(
                col("message").rlike(AUTH_FAILURE),
                lit("AUTH_FAILURE")
            )

            # Authentication Success
            .when(
                col("message").rlike(AUTH_SUCCESS),
                lit("AUTH_SUCCESS")
            )

            # Password Changes
            .when(
                col("message").rlike(PASSWORD_CHANGE),
                lit("PASSWORD_CHANGE")
            )

            # Privileged Commands
            .when(
                col("message").rlike(PRIVILEGED_COMMAND),
                lit("PRIVILEGED_COMMAND")
            )

            # Session Open
            .when(
                col("message").rlike(SESSION_OPEN),
                lit("SESSION_OPEN")
            )

            # Session Close
            .when(
                col("message").rlike(SESSION_CLOSE),
                lit("SESSION_CLOSE")
            )

            # CRON Jobs
            .when(
                col("process").rlike(CRON_JOB),
                lit("CRON_JOB")
            )

            # System Shutdown
            .when(
                col("message").rlike(SYSTEM_SHUTDOWN),
                lit("SYSTEM_SHUTDOWN")
            )

            # System Startup
            .when(
                col("message").rlike(SYSTEM_STARTUP),
                lit("SYSTEM_STARTUP")
            )

            # Default
            .otherwise(
                lit("OTHER")
            )

        )

        # --------------------------------------------------
        # Severity Classification
        # --------------------------------------------------

        .withColumn(

            "severity",

            when(
                col("event_type") == "AUTH_FAILURE",
                lit("HIGH")
            )

            .when(
                col("event_type") == "PASSWORD_CHANGE",
                lit("MEDIUM")
            )

            .when(
                col("event_type") == "PRIVILEGED_COMMAND",
                lit("MEDIUM")
            )

            .when(
                col("event_type") == "SYSTEM_SHUTDOWN",
                lit("MEDIUM")
            )

            .otherwise(
                lit("LOW")
            )

        )

    )