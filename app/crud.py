from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import count

from . import models


def get_marx_quote_by_id(db: Session, id:int):
    return db.query(models.Marx).filter(models.Marx.id == id).first()

def get_engels_quote_by_id(db: Session, id:int):
    return db.query(models.Engels).filter(models.Engels.id == id).first()

def get_trotsky_quote_by_id(db: Session, id:int):
    return db.query(models.Trotsky).filter(models.Trotsky.id == id).first()

def get_tpb_quote_by_id(db: Session, id:int):
    return db.query(models.Tpb).filter(models.Tpb.id == id).first()

def get_marx_quotes_all(db: Session, skip: int = 0, limit: int = 255):
    return db.query(models.Marx).offset(skip).limit(limit).all()

def get_engels_quotes_all(db: Session, skip: int = 0, limit: int = 255):
    return db.query(models.Engels).offset(skip).limit(limit).all()

def get_trotsky_quotes_all(db: Session, skip: int = 0, limit: int = 255):
    return db.query(models.Trotsky).offset(skip).limit(limit).all()

def get_tpb_quotes_all(db: Session, skip: int = 0, limit: int = 255):
    return db.query(models.tpb).offset(skip).limit(limit).all()

def get_marx_quotes_count(db: Session):
    return (db.query(models.Marx).count())

def get_engels_quotes_count(db: Session):
    return (db.query(models.Engels).count())

def get_trotsky_quotes_count(db: Session):
    return (db.query(models.Trotsky).count())

def get_tpb_quotes_count(db: Session):
    return (db.query(models.Trotsky).count())

def get_tpb_quote_named(db: Session, author: str):
    return (db.query(models.Tpb).filter(models.Tpb.author == author).all())
