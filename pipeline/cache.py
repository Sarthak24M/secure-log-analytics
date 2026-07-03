from pipeline.engine import build_pipeline

_spark = None
_classified_logs = None

def get_pipeline():
    global _spark, _classified_logs

    if _spark is None or _classified_logs is None:
        print ("Building pipeline")
        _spark , _classified_logs = build_pipeline()
    
    return _spark, _classified_logs

def stop_pipeline():
    global _spark, _classified_logs
    
    if _spark is not None:
        _spark.stop()

    _spark = None
    _classified_logs = None