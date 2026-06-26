from fastapi import (
    FastAPI,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from database import (
    Base,
    engine,
    get_db
)

from models import Course

from schemas import (
    CourseCreate,
    CourseResponse
)

app=FastAPI(
    title="Course Management API",
    version="1.0"
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )


@app.get("/")
async def root():

    return {
        "message":
        "API running"
    }


@app.post(
    "/api/courses/",
    response_model=CourseResponse
)
async def create_course(
    course:CourseCreate,
    db:AsyncSession=Depends(get_db)
):

    obj=Course(**course.model_dump())

    db.add(obj)

    await db.commit()

    await db.refresh(obj)

    return obj


@app.get(
    "/api/courses/"
)
async def get_courses(
    skip:int=0,
    limit:int=10,
    department_id:int|None=None,
    db:AsyncSession=Depends(get_db)
):

    q=select(Course)

    if department_id:

        q=q.where(
            Course.department_id==
            department_id
        )

    q=q.offset(skip).limit(limit)

    result=await db.execute(q)

    return result.scalars().all()


@app.get(
    "/api/courses/{course_id}"
)
async def get_course(
    course_id:int,
    db:AsyncSession=Depends(get_db)
):

    result=await db.execute(
        select(Course).where(
            Course.id==
            course_id
        )
    )

    course=result.scalar()

    if not course:

        raise HTTPException(
            404,
            "Not Found"
        )

    return course