from typing import List
from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from random import randint
from bs4 import BeautifulSoup
from lxml import etree
import requests
import random


from . import crud, models, schemas
from .database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/api/status')
def API_status_check():
    return {"message": "OK"}

@app.get('/api/status/healthz')
def pod_health_check():
    return {"health":"OK"}

@app.get('/api/status/readyz')
def app_readiness_check():
    return {"ready":"true"}


# Marx
@app.get("/api/marx/all", response_model=List[schemas.Quote])
def get_all_marx_quotes(skip: int = 0, limit: int = 255, db: Session = Depends(get_db)):
    marx_quotes = crud.get_marx_quotes_all(db, skip=skip, limit=limit)
    return marx_quotes

@app.get("/api/marx/id/{id}", response_model=schemas.Quote)
def get_marx_quote_by_id(id: int, db: Session = Depends(get_db)):
    marx_quote = crud.get_marx_quote_by_id(db, id=id)
    if marx_quote is None:
        raise HTTPException(status_code=404, detail="Quote Not Found")
    return marx_quote

@app.get("/api/marx/random", response_model=schemas.Quote)
def get_random_marx_quote(db: Session = Depends(get_db)):
    marx_quote_count = crud.get_marx_quotes_count(db)
    id = randint(1, marx_quote_count)
    marx_quote = crud.get_marx_quote_by_id(db, id)    
    return marx_quote

@app.get("/api/marx/count")
def get_marx_quote_count(db: Session = Depends(get_db)):
    marx_quote_count = crud.get_marx_quotes_count(db)
    return {"count": marx_quote_count}


# Engels
@app.get("/api/engels/all", response_model=List[schemas.Quote])
def get_all_engels_quotes(skip: int = 0, limit: int = 255, db: Session = Depends(get_db)):
    engels_quotes = crud.get_engels_quotes_all(db, skip=skip, limit=limit)
    return engels_quotes

@app.get("/api/engels/id/{id}", response_model=schemas.Quote)
def get_engels_quote_by_id(id: int, db: Session = Depends(get_db)):
    engels_quote = crud.get_engels_quote_by_id(db, id=id)
    if engels_quote is None:
        raise HTTPException(status_code=404, detail="Quote Not Found")
    return engels_quote

@app.get("/api/engels/random", response_model=schemas.Quote)
def get_random_engels_quote(db: Session = Depends(get_db)):
    engels_quote_count = crud.get_engels_quotes_count(db)
    id = randint(1, engels_quote_count)
    engels_quote = crud.get_engels_quote_by_id(db, id)    
    return engels_quote

@app.get("/api/engels/count")
def get_engels_quote_count(db: Session = Depends(get_db)):
    engels_quote_count = crud.get_engels_quotes_count(db)
    return {"count": engels_quote_count}


# Trotsky
@app.get("/api/trotsky/all", response_model=List[schemas.QuoteTrotsky])
def get_all_trotsky_quotes(skip: int = 0, limit: int = 255, db: Session = Depends(get_db)):
    trotsky_quotes = crud.get_trotsky_quotes_all(db, skip=skip, limit=limit)
    return trotsky_quotes

@app.get("/api/trotsky/id/{id}", response_model=schemas.QuoteTrotsky)
def get_trotsky_quote_by_id(id: int, db: Session = Depends(get_db)):
    trotsky_quote = crud.get_trotsky_quote_by_id(db, id=id)
    if trotsky_quote is None:
        raise HTTPException(status_code=404, detail="Quote Not Found")
    return trotsky_quote

@app.get("/api/trotsky/random", response_model=schemas.QuoteTrotsky)
def get_random_trotsky_quote(db: Session = Depends(get_db)):
    trotsky_quote_count = crud.get_trotsky_quotes_count(db)
    id = randint(1, trotsky_quote_count)
    trotsky_quote = crud.get_trotsky_quote_by_id(db, id)    
    return trotsky_quote

@app.get("/api/trotsky/count")
def get_trotsky_quote_count(db: Session = Depends(get_db)):
    trotsky_quote_count = crud.get_trotsky_quotes_count(db)
    return {"count": trotsky_quote_count}

#TPB
@app.get("/api/tpb/all", response_model=List[schemas.QuoteTpb])
def get_all_tpb_quotes(skip: int = 0, limit: int = 255, db: Session = Depends(get_db)):
    tpb_quotes = crud.get_tpb_quotes_all(db, skip=skip, limit=limit)
    return tpb_quotes

@app.get("/api/tpb/id/{id}", response_model=schemas.QuoteTpb)
def get_tpb_quote_by_id(id: int, db: Session = Depends(get_db)):
    tpb_quote = crud.get_tpb_quote_by_id(db, id=id)
    if tpb_quote is None:
        raise HTTPException(status_code=404, detail="Quote Not Found")
    return tpb_quote

@app.get("/api/tpb/random", response_model=schemas.QuoteTpb)
def get_random_tpb_quote(db: Session = Depends(get_db)):
    tpb_quote_count = crud.get_tpb_quotes_count(db)
    id = randint(1, tpb_quote_count)
    tpb_quote = crud.get_tpb_quote_by_id(db, id)    
    return tpb_quote

@app.get("/api/tpb/count")
def get_tpb_quote_count(db: Session = Depends(get_db)):
    tpb_quote_count = crud.get_tpb_quotes_count(db)
    return {"count": tpb_quote_count}

@app.get("/api/tpb/ricky")
def get_ricky_quote(db: Session = Depends(get_db)):
    ricky_quotes = crud.get_tpb_quote_named(db, author="Ricky")
    ricky_quote = random.choice(ricky_quotes)
    return ricky_quote

@app.get("/api/tpb/bubbles")
def get_bubbles_quote(db: Session = Depends(get_db)):
    bubbles_quotes = crud.get_tpb_quote_named(db, author="Bubbles")
    bubbles_quote = random.choice(bubbles_quotes)
    return bubbles_quote

@app.get("/api/tpb/lahey")
def get_lahey_quote(db: Session = Depends(get_db)):
    lahey_quotes = crud.get_tpb_quote_named(db, author="Lahey")
    lahey_quote = random.choice(lahey_quotes)
    return lahey_quote

@app.get("/api/tpb/jroc")
def get_jroc_quote(db: Session = Depends(get_db)):
    jroc_quotes = crud.get_tpb_quote_named(db, author="J-Roc")
    jroc_quote = random.choice(jroc_quotes)
    return jroc_quote

# Bill Hicks
@app.get("/api/hicks/all", response_model=List[schemas.QuoteHicks])
def get_all_hicks_quotes(skip: int = 0, limit: int = 255, db: Session = Depends(get_db)):
    hicks_quotes = crud.get_hicks_quotes_all(db, skip=skip, limit=limit)
    return hicks_quotes

@app.get("/api/hicks/id/{id}", response_model=schemas.QuoteHicks)
def get_hicks_quote_by_id(id: int, db: Session = Depends(get_db)):
    hicks_quote = crud.get_hicks_quote_by_id(db, id=id)
    if hicks_quote is None:
        raise HTTPException(status_code=404, detail="Quote Not Found")
    return hicks_quote

@app.get("/api/hicks/random", response_model=schemas.QuoteHicks)
def get_random_hicks_quote(db: Session = Depends(get_db)):
    hicks_quote_count = crud.get_hicks_quotes_count(db)
    id = randint(1, hicks_quote_count)
    hicks_quote = crud.get_hicks_quote_by_id(db, id)    
    return hicks_quote

@app.get("/api/hicks/count")
def get_hicks_quote_count(db: Session = Depends(get_db)):
    hicks_quote_count = crud.get_hicks_quotes_count(db)
    return {"count": hicks_quote_count}

#FML
@app.get('/api/fml/random')
def get_random_fml():

    url = "https://www.fmylife.com/random"
    
    c_headers = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(url, headers=c_headers)
    
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    dom = etree.HTML(str(soup))
    
    resp_fml_text = dom.xpath('//*[@id="content"]/div/div[1]/article[1]/a/text()')[0]
    resp_your_life_sucks = dom.xpath('//*[@id="content"]/div/div[1]/article/div[2]/div[1]/div/span[2]/text()')
    resp_you_deserved_it = dom.xpath('//*[@id="content"]/div/div[1]/article/div[2]/div[2]/div/span[2]/text()')

    fml_text = resp_fml_text.replace("\n","").strip()
    your_life_sucks = resp_your_life_sucks[0].replace(' ',',')
    you_deserved_it = resp_you_deserved_it[0].replace(' ',',')

    return {
        "text":fml_text, 
        "your_life_sucks":your_life_sucks,
        "you_deserved_it":you_deserved_it 
        }
