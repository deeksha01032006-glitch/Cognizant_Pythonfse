from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship
)

Base = declarative_base()

# Replace YOUR_PASSWORD
engine = create_engine(
    "mysql+mysqlconnector://root:deeksha01@localhost/college_db_orm",
    echo=True
)


# -------------------------
# Department
# -------------------------
class Department(Base):

    __tablename__ = "departments"

    department_id = Column(
        Integer,
        primary_key=True
    )

    dept_name = Column(
        String(100),
        nullable=False
    )

    students = relationship(
        "Student",
        back_populates="department"
    )

    courses = relationship(
        "Course",
        back_populates="department"
    )

    professors = relationship(
        "Professor",
        back_populates="department"
    )


# -------------------------
# Student
# -------------------------
class Student(Base):

    __tablename__ = "students"

    student_id = Column(
        Integer,
        primary_key=True
    )

    first_name = Column(
        String(50)
    )

    last_name = Column(
        String(50)
    )

    email = Column(
        String(100),
        unique=True
    )

    enrollment_year = Column(
        Integer
    )

    department_id = Column(
        Integer,
        ForeignKey(
            "departments.department_id"
        )
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )


# -------------------------
# Course
# -------------------------
class Course(Base):

    __tablename__ = "courses"

    course_id = Column(
        Integer,
        primary_key=True
    )

    course_name = Column(
        String(100)
    )

    department_id = Column(
        Integer,
        ForeignKey(
            "departments.department_id"
        )
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )


# -------------------------
# Enrollment
# -------------------------
class Enrollment(Base):

    __tablename__ = "enrollments"

    enrollment_id = Column(
        Integer,
        primary_key=True
    )

    student_id = Column(
        Integer,
        ForeignKey(
            "students.student_id"
        )
    )

    course_id = Column(
        Integer,
        ForeignKey(
            "courses.course_id"
        )
    )

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )


# -------------------------
# Professor
# -------------------------
class Professor(Base):

    __tablename__ = "professors"

    professor_id = Column(
        Integer,
        primary_key=True
    )

    prof_name = Column(
        String(100)
    )

    department_id = Column(
        Integer,
        ForeignKey(
            "departments.department_id"
        )
    )

    department = relationship(
        "Department",
        back_populates="professors"
    )


print("Creating tables...")

Base.metadata.create_all(engine)

print("All tables created successfully.")