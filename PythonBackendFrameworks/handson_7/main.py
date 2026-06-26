from fastapi import (
    FastAPI,
    HTTPException,
    status,
    BackgroundTasks
)

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API for Courses",
    version="1.0",
    contact={
        "name": "Deeksha"
    }
)

# Temporary data storage
courses = [
    {
        "id": 1,
        "name": "Python",
        "code": "CS101",
        "credits": 4,
        "department_id": 1
    }
]


# ROOT
@app.get("/")
async def root():
    return {"message": "API Running"}


# GET ALL COURSES
@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"]
)
async def get_courses():
    return courses


# GET COURSE BY ID
@app.get(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def get_course(id: int):

    for course in courses:
        if course["id"] == id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# CREATE COURSE
@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Created course successfully"
)
async def create_course(
        course: CourseCreate):

    new_course = {
        "id": len(courses) + 1,
        **course.dict()
    }

    courses.append(new_course)

    return new_course


# UPDATE COURSE
@app.put(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def update_course(
        id: int,
        course: CourseUpdate):

    for c in courses:

        if c["id"] == id:

            update = course.dict(
                exclude_unset=True
            )

            c.update(update)

            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# DELETE COURSE
@app.delete(
    "/api/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(id: int):

    for i in range(len(courses)):

        if courses[i]["id"] == id:

            courses.pop(i)

            return

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# GET STUDENTS
@app.get(
    "/api/courses/{id}/students"
)
async def get_students(id: int):

    return {
        "course_id": id,
        "students": [
            "Student A",
            "Student B"
        ]
    }


# BACKGROUND TASK
def send_confirmation_email(
        student_email: str):

    print(
        f"Sending confirmation to {student_email}"
    )


# ENROLLMENT
@app.post(
    "/api/enrollments/",
    status_code=201,
    tags=["Enrollments"]
)
async def enroll(
        data: dict,
        background_tasks: BackgroundTasks):

    background_tasks.add_task(
        send_confirmation_email,
        data["student_email"]
    )

    return {
        "message":
        "Enrollment created"
    }