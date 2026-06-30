from pyspark.sql.functions import (
    col,
    regexp_extract,
    when,
    coalesce
)

from spark.patterns import *


def extract_username():

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

    return coalesce(
        username_user,
        username_password,
        username_exec
    )


def extract_target_user():

    target_user = when(
        regexp_extract(col("message"), TARGET_USER, 1) != "",
        regexp_extract(col("message"), TARGET_USER, 1)
    )

    target_exec = when(
        regexp_extract(col("message"), TARGET_USER_EXEC, 1) != "",
        regexp_extract(col("message"), TARGET_USER_EXEC, 1)
    )

    return coalesce(
        target_user,
        target_exec
    )


def extract_command():

    return regexp_extract(
        col("message"),
        COMMAND,
        1
    )


def extract_uid():

    return regexp_extract(
        col("message"),
        UID,
        1
    )


def extract_tty():

    return regexp_extract(
        col("message"),
        TTY,
        1
    )


def extract_cwd():

    return regexp_extract(
        col("message"),
        CWD,
        1
    )


def extract_session():

    return regexp_extract(
        col("message"),
        SESSION_ID,
        1
    )


def extract_ip():

    return regexp_extract(
        col("message"),
        IP,
        1
    )