from flask import Flask, jsonify

app = Flask(__name__)

courses = {
    1: {
        "id": 1,
        "name": "Python"
    },
    2: {
        "id": 2,
        "name": "FastAPI"
    }
}


@app.route("/api/courses/<int:id>/")
def get_course(id):

    course = courses.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    return jsonify(course)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=True
    )