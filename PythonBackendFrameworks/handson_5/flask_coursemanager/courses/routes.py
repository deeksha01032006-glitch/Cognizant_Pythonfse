from flask import Blueprint
from flask import jsonify
from flask import request

from extensions import db

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


@courses_bp.route("/", methods=["GET"])
def get_courses():

    from courses.models import Course

    courses = Course.query.all()

    return jsonify(
        [
            c.to_dict()
            for c in courses
        ]
    )


@courses_bp.route("/", methods=["POST"])
def create_course():

    from courses.models import Course

    data = request.json

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"]
    )

    db.session.add(
        course
    )

    db.session.commit()

    return jsonify(
        course.to_dict()
    )


@courses_bp.route(
    "/<int:id>",
    methods=["GET"]
)
def get_course(id):

    from courses.models import Course

    course = Course.query.get_or_404(id)

    return jsonify(
        course.to_dict()
    )
@courses_bp.route(
    "/<int:id>",
    methods=["PUT"]
)
def update_course(id):

    from extensions import db
    from courses.models import Course

    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]

    db.session.commit()

    return jsonify(
        course.to_dict()
    )