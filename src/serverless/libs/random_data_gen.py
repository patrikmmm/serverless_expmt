'''Generates a lif of random customers'''
import random
import string
import serverless.libs.customer as cust


def get_random_string(length: int):
    '''generates a random string'''
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    # print("Random string of length", length, "is:", result_str)


def get_random_customer(ident: int, mode: str):
    '''generates a random customer'''
    if mode == "random":
        ident = random.randint(1, 99999)
    deets = cust.Details(var1=123, var2="lol")
    customer = cust.CustomerObject(
                        id=ident,
                        name=get_random_string(12),
                        age=random.randint(1, 99),
                        details=deets
                    )
    return customer


def gen_customer_list(length):
    '''generates a list of random customers'''
    customers = []
    for var in range(length):
        customers.append(get_random_customer())

    return customers
