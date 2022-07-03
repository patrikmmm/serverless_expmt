'''quick and dirty API example using FastAPI'''
from fastapi import FastAPI
from mangum import Mangum
import serverless.libs.random_data_gen as rdg
import serverless.libs.customer as co
import serverless.libs.connector as cntr

CONNECTION_STRING = "mongodb://docker:mongopw@localhost:55000"
__version__ = '0.1.0'

app = FastAPI()

#connection = cntr.connect_db(CONNECTION_STRING, "SCV")
#collection_conn = cntr.get_collection(connection, "scv_data")


@app.get("/", response_model=co.CustomerObject)
def get_root():
    '''Dirty Demo'''
    return rdg.get_random_customer(1, "random")


@app.post("/customers/")
def post_cust(customer: co.CustomerObject):
    #cntr.add_customer(collection_conn, customer)
    return customer


handler = Mangum(app)
