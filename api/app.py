from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    return {
        "message": "Secure Log Analytics API is running."
    }


@app.route("/api/summary")
def summary():

    return {
        "status": "success",
        "project": "Secure Log Analytics",
        "version": "1.0"
    }


if __name__ == "__main__":
    app.run(debug=True)