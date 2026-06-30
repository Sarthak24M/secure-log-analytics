from pyspark.sql.functions import (
    col,
    regexp_extract,
    when,
    coalesce,
    lit
)

from spark.patterns import (
    USERNAME_USER,
    USERNAME_PASSWORD,
    USERNAME_EXEC,
    TARGET_USER,
    TARGET_USER_EXEC,
    COMMAND,
    IP
)


def extract_fields(df):

    # -------------------------
    # Username extraction
    # -------------------------

    username_user = when(
        regexp_extract(col("message"), USERNAME_USER, 1) != "",
        regexp_extract(col("message"), USERNAME_USER, 1)
    )

    username_password = when(
        regexp_extract(col("message"), USERNAME_PASSWORD, 1) != "",
        regexp_extract(col("message"), USERNAME_PASSWORD, 1)
    )

    username_exec = when(
        regexp_extract(col("message"), USERNAME_EXEC, 1) != "",
        regexp_extract(col("message"), USERNAME_EXEC, 1)
    )

    return (

        df

        .withColumn(
            "username",
            coalesce(
                username_user,
                username_password,
                username_exec
            )
        )

        .withColumn(
            "target_user",
            regexp_extract(
                col("message"),
                TARGET_USER,
                1
            )
        )

        .withColumn(
            "ip_address",
            regexp_extract(
                col("message"),
                IP,
                1
            )
        )

        .withColumn(
            "command",
            regexp_extract(
                col("message"),
                COMMAND,
                1
            )
        )

        .withColumn(
            "auth_status",
            when(
                col("message").rlike("FAILED|failure"),
                lit("FAILED")
            )
            .when(
                col("message").rlike("session opened"),
                lit("SUCCESS")
            )
            .when(
                col("message").rlike("accepted"),
                lit("SUCCESS")
            )
            .otherwise(
                lit("UNKNOWN")
            )
        )

    )