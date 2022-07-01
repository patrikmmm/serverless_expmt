'''quick and dirty API example using FastAPI'''
from fastapi import FastAPI
from mangum import Mangum
__version__ = '0.1.0'

app = FastAPI()

@app.get("/")
def get_root():
    '''Dirty Demo'''
    return {"message:": "FastAPI running in a Lambda function"}

handler = Mangum(app)
