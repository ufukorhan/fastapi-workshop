from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost/fastapi' # in the future this field will be hidden

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency:  It allows us to securely create a session and close it every time a request is sent!   
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()