from sqlalchemy import create_engine
from models import Base

engine = create_engine(
"mysql+mysqlconnector://root:deeksha01@localhost/college_db_orm",
echo=True
)

print("Creating tables...")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("Tables created")