from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# SQLALCHEMY_DATABASE_URL = "postgresql://default:4dCScpNLDP9g@ep-green-sun-28780142.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb"
SQLALCHEMY_DATABASE_URL = "postgresql://ntue:ntuedtd@db:5432/ntue"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()