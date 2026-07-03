from pyspark.sql.functions import (count, 
                                   col,
                                   when,
                                   sum as spark_sum
                                   )

def event_distribution(df):
    return (
        df
        .groupBy("event_type")

        .agg(

            count("*").alias("total_events")

        )

        .orderBy(
            "total_events",
            ascending = False
        )
    )

def authentication_summary(df):

    return (

        df

        .groupBy(

            "auth_status"
        )

        .agg(
            count("*").alias("total_events")
        )

        .orderBy(
            "total_events",
            ascending=False
        )

    )

def top_user(df):
    return (

        df
        .filter(
            col("username").isNotNull()
        )
        .groupBy(
            "username"
        )

        .agg(
            count("*").alias("total_events")
        )

        .orderBy(
            col("total_events").desc()
        )
    )

def top_process (df):
    return (

        df

        .filter(
            col("process").isNotNull()
        )

        .groupBy(
            "process"
        )

        .agg(
            count("*").alias("total_events")
        )

        .orderBy(
            col("total_events").desc()
        )

    )
def dashboard_summary(df):
    result = (

        df

        .agg(

            count("*").alias("total_events"),

            spark_sum(
                when(
                    col("event_type") == "AUTH_FAILURE",
                    1
                ).otherwise(0)
            ).alias("authentication_failures"),

            spark_sum(
                when(
                    col("event_type") == "PASSWORD_CHANGE",
                    1
                ).otherwise(0)
            ).alias("password_changes"),

            spark_sum(
                when(
                    col("severity") == "HIGH",
                    1
                ).otherwise(0)
            ).alias("high_severity_alerts"),

            spark_sum(
                when(
                    col("process").isin(
                        "sudo",
                        "pkexec",
                        "su",
                        "passwd"
                    ),
                    1
                ).otherwise(0)
            ).alias("privileged_commands")

        )

    )

    return result.first().asDict()
