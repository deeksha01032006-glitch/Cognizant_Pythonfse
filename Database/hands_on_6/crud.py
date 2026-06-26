from models import *
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, joinedload

# ----------------------
# DATABASE CONNECTION
# ----------------------
engine = create_engine(
    "mysql+mysqlconnector://root:deeksha01@localhost/college_db_orm",
    echo=False
)

Session = sessionmaker(bind=engine)
session = Session()

print("Creating tables...")
Base.metadata.create_all(engine)
print("All tables created successfully.")

# ----------------------
# CLEAR OLD DATA
# ----------------------
try:
    session.query(Enrollment).delete()
    session.query(Student).delete()
    session.query(Course).delete()
    session.query(Department).delete()

    session.commit()

    session.execute(text("ALTER TABLE enrollments AUTO_INCREMENT=1"))
    session.execute(text("ALTER TABLE students AUTO_INCREMENT=1"))
    session.execute(text("ALTER TABLE courses AUTO_INCREMENT=1"))
    session.execute(text("ALTER TABLE departments AUTO_INCREMENT=1"))

    session.commit()

    print("Old data deleted")

except Exception as e:
    session.rollback()
    print("Delete Error:", e)
# ----------------------
# INSERT DEPARTMENTS
# ----------------------

cs = Department(dept_name="Computer Science")
ec = Department(dept_name="Electronics")
me = Department(dept_name="Mechanical")

session.add_all([cs, ec, me])
session.commit()

print("Departments inserted")


# ----------------------
# INSERT STUDENTS
# ----------------------

s1 = Student(
    first_name="Deeksha",
    last_name="S",
    email="d1@gmail.com",
    enrollment_year=2022,
    department_id=cs.department_id
)

s2 = Student(
    first_name="Anu",
    last_name="R",
    email="a1@gmail.com",
    enrollment_year=2023,
    department_id=cs.department_id
)

s3 = Student(
    first_name="John",
    last_name="P",
    email="j1@gmail.com",
    enrollment_year=2021,
    department_id=ec.department_id
)

s4 = Student(
    first_name="Sara",
    last_name="T",
    email="s1@gmail.com",
    enrollment_year=2024,
    department_id=me.department_id
)

s5 = Student(
    first_name="Kavi",
    last_name="M",
    email="k1@gmail.com",
    enrollment_year=2022,
    department_id=ec.department_id
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()

print("Students inserted")

# ----------------------
# INSERT COURSES
# ----------------------
c1 = Course(
    course_name="DBMS",
    department_id=cs.department_id
)

c2 = Course(
    course_name="Python",
    department_id=cs.department_id
)

c3 = Course(
    course_name="Java",
    department_id=ec.department_id
)

session.add_all([c1, c2, c3])
session.commit()

print("Courses inserted")


# ----------------------
# INSERT ENROLLMENTS
# ----------------------

e1 = Enrollment(student=s1, course=c1)
e2 = Enrollment(student=s2, course=c2)
e3 = Enrollment(student=s3, course=c3)
e4 = Enrollment(student=s1, course=c2)

session.add_all([e1, e2, e3, e4])
session.commit()

print("Enrollments inserted")


# ----------------------
# READ
# ----------------------
print("\nComputer Science Students")

students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name ==
        "Computer Science"
    )
)

for s in students:
    print(s.first_name, s.last_name)


# ----------------------
# UPDATE
# ----------------------
student = (
    session.query(Student)
    .filter_by(email="d1@gmail.com")
    .first()
)

if student:
    student.enrollment_year = 2025
    session.commit()

print("\nUpdated")


# ----------------------
# DELETE
# ----------------------
record = session.query(Enrollment).first()

if record:
    session.delete(record)
    session.commit()

print("Deleted one enrollment")


# ----------------------
# WITHOUT JOINEDLOAD
# ----------------------
print("\nWITHOUT joinedload")

data = session.query(
    Enrollment
).all()

for e in data:
    print(
        e.student.first_name,
        e.course.course_name
    )


# ----------------------
# WITH JOINEDLOAD
# ----------------------
print("\nWITH joinedload")

data = (
    session.query(
        Enrollment
    )
    .options(
        joinedload(
            Enrollment.student
        ),
        joinedload(
            Enrollment.course
        )
    )
    .all()
)

for e in data:
    print(
        e.student.first_name,
        e.course.course_name
    )

session.close()

print("\nProgram executed successfully")