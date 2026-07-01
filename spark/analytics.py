from pyspark.sql.functions import count, col

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
