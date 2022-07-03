'''Generates a lif of random customers'''
import random
import string

def get_random_string(length):
    '''generates a random string'''
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    # print("Random string of length", length, "is:", result_str)

def get_random_customer():
    '''generates a random customer'''
    customer = {
        "id":random.randint(1,99999),
        "name":get_random_string(12),
        "age":random.randint(1,99),
        "details":{
            "var1":1,
            "var2":"Finland"
        }
    }
    return customer

def gen_customer_list(length):
    '''generates a list of random customers'''
    customers = []
    for x in range(length):
       customers.append(get_random_customer())

    return customers



