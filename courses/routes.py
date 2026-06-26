from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = []


# GET ALL
@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)


# POST
@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    course = {
        "id": len(courses)+1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(course)

    return jsonify(course), 201


# GET BY ID
@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):

    for course in courses:

        if course["id"] == course_id:
            return jsonify(course)

    return jsonify({
        "error": "Course not found"
    }), 404


# PUT
@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    data = request.get_json()

    for course in courses:

        if course["id"] == course_id:

            course.update(data)

            return jsonify(course)

    return jsonify({
        "error": "Course not found"
    }), 404


# DELETE
@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    for course in courses:

        if course["id"] == course_id:

            courses.remove(course)

            return jsonify({
                "message": "Deleted"
            })

    return jsonify({
        "error": "Course not found"
    }), 404