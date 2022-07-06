'''This script defines the standard customer representation for our app'''
from pydantic import BaseModel, Field


class Details(BaseModel):
    '''random details'''
    var1: int
    var2: str


class CustomerObject(BaseModel):
    '''main customer object'''
    id: int
    name: str | None = Field(title="The name of the customer")
    age: int | None = None
    details: Details
