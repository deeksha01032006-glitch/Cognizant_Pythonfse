from flask import Flask
from extensions import db, migrate


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coursemanager.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    migrate.init_app(app, db)

    from courses.routes import courses_bp

    app.register_blueprint(courses_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)