'''This script defines the standard customer representation for our app'''
from pydantic import BaseModel


class Details(BaseModel):
    '''random details'''
    var1: int
    var2: str


class CustomerObject(BaseModel):
    '''main customer object'''
    id: int
    name: str
    age: int
    details: Details

# deets =  Details(var1=123, var2="lol")
# customer = CustomerObject(id=123,name="paddy",age=33,details=deets)

# print(customer.dict())
