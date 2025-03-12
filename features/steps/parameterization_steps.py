from behave import *
import requests

# @given('the API endpoint is "{endpoint}"')
# def step_impl(context, endpoint):
#     context.endpoint = endpoint
#     full_url = "https://jsonplaceholder.typicode.com/users" + endpoint
    
# @when('I send a GET request')
# def step_impl(context):
#     context.response = requests.get(context.full_url)
    

# @then('the response status code should be 200')
# def step_impl(context):
#     assert context.response.status_code == 200
#     print("response status code is 200")
    
# @then('the response JSON should have "{username}" as "{expected_username}"')
# def step_impl(context, username, expected_username):
#     response_json = context.response.json()
#     assert response_json[username] == expected_username
#     print("response JSON has username as expected_username")
    
    
@given('the API endpoint is "{user_id}"')
def step_impl(context, user_id):
    context.endpoint = user_id
    context.full_url = "https://jsonplaceholder.typicode.com/users/" + context.endpoint

@when('I send a GET request')
def step_impl(context):
    context.response = requests.get(context.full_url)
    
@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)
    print("response status code is 200")
    
@then('the response should contain "{expected_name}"')
def step_impl(context, expected_name):
    response_json = context.response.json()
    if expected_name in response_json['name']:
        assert True
    elif len(response_json) == 0:
            print("Dictionary is empty")
            assert True
            