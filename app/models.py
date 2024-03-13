from sqlalchemy import Column, String, Integer

from .database import Base


class Marx(Base):
    __tablename__ = "marx"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(16))
    quote = Column(String(2048))
    source = Column(String(128))
    year = Column(Integer)

class Engels(Base):
    __tablename__ = "engels"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(16))
    quote = Column(String(2048))
    source = Column(String(128))
    year = Column(Integer)

class Trotsky(Base):
    __tablename__ = "trotsky"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(16))
    quote = Column(String(2048))
    source = Column(String(128))
    topic = Column(String(64))
    year = Column(Integer)

class Tpb(Base):
    __tablename__ = "tpb"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(16))
    quote = Column(String(2048))
