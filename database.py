from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file peru. student-api folder lo create aithundi
SQLALCHEMY_DATABASE_URL = "sqlite:///./kuppam.db"

# Engine create cheyyadam. SQLite kosam check_same_thread=False kavali
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Database session create cheyyadaniki
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models ki base class. Dini nunchi models inherit avthay
Base = declarative_base()

# Dependency: FastAPI routes lo db session teesukodaniki
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()