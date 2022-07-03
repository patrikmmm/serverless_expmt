'''quick and dirty API example using FastAPI'''
from fastapi import FastAPI
from mangum import Mangum
from random_data_gen import *
__version__ = '0.1.0'

print(gen_customer_list(5))

app = FastAPI()


@app.get("/")
def get_root():
    '''Dirty Demo'''
    return {"message:": "falafel sucks"}

handler = Mangum(app)


