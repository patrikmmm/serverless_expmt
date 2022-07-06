'''quick and dirty API example using FastAPI'''
from fastapi import FastAPI
from mangum import Mangum
import serverless.libs.random_data_gen as rdg
import serverless.libs.customer as co
import serverless.libs.connector as cntr
import uvicorn #for debugging only

__version__ = '0.1.0'
#CONNECTION_STRING = "mongodb://docker:mongopw@host.docker.internal:55000"
CONNECTION_STRING = "mongodb://docker:mongopw@localhost:55000" #for debugging only

app = FastAPI()


@app.get("/", response_model=co.CustomerObject)
def get_root():
    '''Dirty Demo'''
    return rdg.get_random_customer(1, "random")


@app.get("/customers/{id}", response_model=co.CustomerObject)
def get_customer(id: int):
    connection = cntr.connect_db(CONNECTION_STRING, "SCV")
    collection_conn = cntr.get_collection(connection, "scv_data")
    result = cntr.find_customer_by_id(collection_conn, id)
    return result


@app.post("/customers/")
def post_cust(customer: co.CustomerObject):
    connection = cntr.connect_db(CONNECTION_STRING, "SCV")
    collection_conn = cntr.get_collection(connection, "scv_data")
    customer_dict = customer.dict()
    cntr.add_customer(collection_conn, customer_dict)
    results = {"customer": customer}
    return results


handler = Mangum(app)

#debugger code
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
