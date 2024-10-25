from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.environ['FAST_API_MYSQL']

engine = create_engine(DATABASE_URL,
    pool_size=10,          # Adjust based on load
    max_overflow=20,       # Max extra connections
    pool_recycle=28000,    # Recycle connections within MySQL's timeout
    pool_timeout=30        # Optional timeout for retrieving a connection)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
