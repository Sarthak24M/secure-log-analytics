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