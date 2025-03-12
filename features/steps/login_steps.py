import logging
from behave import given, when, then
import requests
from utilities.readfromglobalconf import *
from utilities.resources import *
from utilities.payloads import *

logging.basicConfig(level=logging.INFO)

@given('the login credentails')
def step_impl(context):
    url = readfromglobalconf('API', 'url')
    endpoint = APIResources.login
    context.full_url = url + endpoint
    context.payload = loginPayload()
    print("login details are passed")
    

@when('do the login')
def step_impl(context):
    context.response = requests.post(context.full_url, json=context.payload)
    #print("login is done")
    logging.info("login is done")

@then('login is successfull')
def step_impl(context):
    assert context.response.status_code == 200
    print("login is successfull")


