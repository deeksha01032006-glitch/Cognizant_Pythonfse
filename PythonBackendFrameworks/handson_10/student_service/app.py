from flask import Flask
from flask import request
from flask import jsonify

import requests

app = Flask(__name__)


@app.route(
"/api/students/<int:id>/enroll",
methods=["POST"]
)

def enroll(id):

    data=request.json

    course_id=data["course_id"]

    try:

        r=requests.get(
f"http://127.0.0.1:5001/api/courses/{course_id}/"
)

    except:

        return jsonify(
{
"error":
"Course Service unavailable"
}
),503

    if r.status_code!=200:

        return jsonify(
{
"error":
"Course not found"
}
),404


    return jsonify(
{
"message":
"Enrollment successful"
}
)


if __name__=="__main__":

    app.run(
        port=5002,
        debug=True
    )