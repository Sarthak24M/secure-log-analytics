from pyspark.sql.functions import (
    col,
    when,
    lit
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
                col("message").rlike("(?i)failed|failure|authentication failure"),
                lit("AUTH_FAILURE")
            )

            # Password Changes
            .when(
                col("message").rlike("(?i)password.*changed|changed by"),
                lit("PASSWORD_CHANGE")
            )

            # Privileged Commands
            .when(
                col("message").rlike("(?i)executing command"),
                lit("PRIVILEGED_COMMAND")
            )

            # Session Open
            .when(
                col("message").rlike("(?i)session opened"),
                lit("SESSION_OPEN")
            )

            # Session Close
            .when(
                col("message").rlike("(?i)session closed"),
                lit("SESSION_CLOSE")
            )

            # CRON Jobs
            .when(
                col("process").rlike("(?i)^cron"),
                lit("CRON_JOB")
            )

            # System Shutdown
            .when(
                col("message").rlike("(?i)powering down|power off|shutdown"),
                lit("SYSTEM_SHUTDOWN")
            )

            # System Startup
            .when(
                col("message").rlike("(?i)startup|system boot|boot completed"),
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