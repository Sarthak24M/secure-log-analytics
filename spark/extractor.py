from pyspark.sql.functions import (
    when,
    col,
    lit
)

from spark.extractors import *


def extract_fields(df):

    return (

        df

        .withColumn(
            "username",
            extract_username()
        )

        .withColumn(
            "target_user",
            extract_target_user()
        )

        .withColumn(
            "command",
            extract_command()
        )

        .withColumn(
            "uid",
            extract_uid()
        )

        .withColumn(
            "tty",
            extract_tty()
        )

        .withColumn(
            "cwd",
            extract_cwd()
        )

        .withColumn(
            "session_id",
            extract_session()
        )

        .withColumn(
            "ip_address",
            extract_ip()
        )

        .withColumn(
            "auth_status",

            when(
                col("message").rlike("FAILED|failure"),
                lit("FAILED")
            )

            .when(
                col("message").rlike(
                    "session opened|accepted|password changed|Executing command"
                ),
                lit("SUCCESS")
            )

            .otherwise(
                lit("UNKNOWN")
            )

        )

    )