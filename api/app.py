from flask import Flask
from api.services import get_summary
from api.services import get_analytics
from api.services import get_detections

app = Flask(__name__)


@app.route("/")
def home():

    return {
        "message": "Secure Log Analytics API is running."
    }


@app.route("/api/summary")
def summary():

    return get_summary()

@app.route("/api/analytics")
def analytics():

    return get_analytics()

@app.route("/api/detections")
def detections():

    return get_detections()

if __name__ == "__main__":
    app.run(debug=True)

