from fastapi import FastAPI,Depends,HTTPException,Response,status
from sqlalchemy.orm import Session
from database import get_db,engine
from models import Base,Course
from schemas import CourseCreate,CourseUpdate,CourseResponse

Base.metadata.create_all(bind=engine)

app=FastAPI(
title="Course API V1",
description="REST API with Pagination",
version="1.0",
contact={
"name":"Deeksha"
}
)

# URL Versioning
# Alternative:
# Header versioning:
# Accept: application/vnd.api+json;version=1


def error_response(code,msg):
    return {
        "error":{
            "code":code,
            "message":msg,
            "field":None
        }
    }


@app.get("/")
def root():
    return {"message":"Handson 8 Running"}


# CREATE
@app.post(
"/api/v1/courses/",
status_code=201,
response_model=CourseResponse
)
def create_course(
course:CourseCreate,
response:Response,
db:Session=Depends(get_db)
):

    new_course=Course(**course.dict())

    db.add(new_course)

    db.commit()

    db.refresh(new_course)

    response.headers[
"Location"
]=f"/api/v1/courses/{new_course.id}"

    return new_course


# GET PAGINATION
@app.get("/api/v1/courses/")
def get_courses(
page:int=1,
page_size:int=2,
search:str="",
db:Session=Depends(get_db)
):

    query=db.query(Course)

    if search:
        query=query.filter(
            Course.name.contains(search)
        )

    total=query.count()

    skip=(page-1)*page_size

    data=query.offset(skip).limit(page_size).all()

    next_url=None
    previous=None

    if skip+page_size<total:
        next_url=f"/api/v1/courses/?page={page+1}"

    if page>1:
        previous=f"/api/v1/courses/?page={page-1}"

    return{
        "count":total,
        "next":next_url,
        "previous":previous,
        "results":data
    }


# GET
@app.get(
"/api/v1/courses/{id}",
response_model=CourseResponse
)
def get_course(
id:int,
db:Session=Depends(get_db)
):

    course=db.query(
Course
).filter(
Course.id==id
).first()

    if not course:
        raise HTTPException(
404,
error_response(
"NOT_FOUND",
f"Course {id} not found"
)
)

    return course


# PUT
@app.put(
"/api/v1/courses/{id}",
response_model=CourseResponse
)
def update_course(
id:int,
course:CourseCreate,
db:Session=Depends(get_db)
):

    c=db.query(
Course
).filter(
Course.id==id
).first()

    if not c:
        raise HTTPException(
404,
error_response(
"NOT_FOUND",
"Course not found"
)
)

    c.name=course.name
    c.code=course.code
    c.credits=course.credits

    db.commit()

    return c


# PATCH
@app.patch(
"/api/v1/courses/{id}"
)
def patch_course(
id:int,
course:CourseUpdate,
db:Session=Depends(get_db)
):

    c=db.query(
Course
).filter(
Course.id==id
).first()

    if not c:
        raise HTTPException(
404,
error_response(
"NOT_FOUND",
"Course not found"
)
)

    for k,v in course.dict(
exclude_unset=True
).items():
        setattr(c,k,v)

    db.commit()

    return c


# DELETE
@app.delete(
"/api/v1/courses/{id}",
status_code=204
)
def delete_course(
id:int,
db:Session=Depends(get_db)
):

    c=db.query(
Course
).filter(
Course.id==id
).first()

    if not c:
        raise HTTPException(
404,
error_response(
"NOT_FOUND",
"Course not found"
)
)

    db.delete(c)

    db.commit()