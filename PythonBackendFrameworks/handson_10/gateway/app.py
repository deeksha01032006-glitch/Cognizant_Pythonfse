from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route(
"/api/courses/<path:path>"
)
def course(path):

    r = requests.get(
        f"http://127.0.0.1:5001/api/courses/{path}"
    )

    return (
        r.content,
        r.status_code,
        r.headers.items()
    )


@app.route(
"/api/students/<path:path>",
methods=["POST"]
)
def student(path):

    r = requests.post(

        f"http://127.0.0.1:5002/api/students/{path}",

        json=request.json

    )

    return (
        r.content,
        r.status_code,
        r.headers.items()
    )


if __name__=="__main__":

    app.run(
        port=5000,
        debug=True
    )