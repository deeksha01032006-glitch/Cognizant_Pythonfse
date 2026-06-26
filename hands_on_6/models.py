from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    dept_name = Column(
        String(50),
        nullable=False
    )

    students = relationship(
        "Student",
        back_populates="department"
    )


class Student(Base):
    __tablename__ = "students"

    student_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name = Column(String(50))
    last_name = Column(String(50))

    email = Column(
        String(100),
        unique=True
    )

    enrollment_year = Column(Integer)

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


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    course_name = Column(
        String(50)
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )


class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
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