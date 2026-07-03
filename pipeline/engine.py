from pipeline.spark_session import create_spark_session
from pipeline.reader import read_logs
from pipeline.parser import parse_logs
from pipeline.extractor import extract_fields
from pipeline.classifier import classify_events


def build_pipeline():

    spark = create_spark_session()

    logs = read_logs(
        spark,
        "data/raw/auth.log"
    )

    parsed_logs = parse_logs(logs)

    extracted_logs = extract_fields(parsed_logs)

    classified_logs = classify_events(extracted_logs)

    return spark, classified_logs
