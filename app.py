from flask import Flask # , request, Response

app = Flask(__name__)

@app.route("/")
def health_check():
    """
    This function is an endpoint for checking the health of the application
    """
    return "ok"

