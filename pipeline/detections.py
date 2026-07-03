from pyspark.sql.functions import col,count

def high_severity_alerts(df):

    return (

        df

        .filter(
            col("severity") == "HIGH"
        )

        .select(
            "timestamp",
            "username",
            "process",
            "event_type",
            "severity",
            "message"
        )

    )

def privileged_activity(df):

    return (

        df

        .filter(

            col("process").isin(

                "sudo",

                "pkexec",

                "su",

                "passwd"

            )

        )

        .select(

            "timestamp",

            "username",

            "process",

            "command",

            "event_type",

            "severity"

        )

    )

def password_change_alerts(df):

    return (

        df

        .filter(

            col("event_type") == "PASSWORD_CHANGE"

        )

    )

def authentication_failures(df):

    return (

        df

        .filter(

            col("event_type") == "AUTH_FAILURE"

        )

    )

def brute_force_detection(df):

    return (

        df

        .filter(
            col("event_type") == "AUTH_FAILURE"
        )

        .groupBy(
            "target_user"
        )

        .agg(
            count("*").alias("failed_attempts")
        )

        .filter(
            col("failed_attempts") >= 3
        )

        .orderBy(
            col("failed_attempts").desc()
        )

    )

from pyspark.sql.functions import col, count


def excessive_sudo_detection(df):

    return (

        df

        .filter(
            col("event_type") == "PRIVILEGED_COMMAND"
        )

        .groupBy(
            "username"
        )

        .agg(
            count("*").alias("privileged_commands")
        )

        .filter(
            col("privileged_commands") >= 3
        )

        .orderBy(
            col("privileged_commands").desc()
        )

    )

def root_activity_detection(df):

    return (

        df

        .filter(
            (col("username") == "root") |
            (col("target_user") == "root") |
            (col("uid") == "0")
        )

        .filter(
            col("process") != "CRON"
        )

        .select(
            "timestamp",
            "username",
            "target_user",
            "process",
            "event_type",
            "command",
            "severity"
        )

        .orderBy("timestamp")

    )