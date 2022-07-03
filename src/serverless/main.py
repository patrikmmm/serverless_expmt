'''quick and dirty API example using FastAPI'''
from fastapi import FastAPI
from mangum import Mangum
import libs.random_data_gen as rdg
import libs.customer as co

__version__ = '0.1.0'

app = FastAPI()


@app.get("/", response_model=co.CustomerObject)
def get_root():
    '''Dirty Demo'''
    return rdg.get_random_customer(1, "random")


@app.post("/customers/")
def post_cust(customer: co.CustomerObject):
    return customer


handler = Mangum(app)
