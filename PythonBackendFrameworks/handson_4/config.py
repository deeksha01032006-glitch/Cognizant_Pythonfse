class Config:

    SECRET_KEY = "secret"

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///courses.db"
    )