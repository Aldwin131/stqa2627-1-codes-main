from behave import given, when, then
import requests

@given('the counter is reset')
def step_impl(context):
    response = requests.post(f"{context.base_url}/reset")
    assert response.status_code == 200

@when('a user clicks the "Hit" button')
def step_impl(context):
    response = requests.post(f"{context.base_url}/hit")
    assert response.status_code == 200

@then('the counter should be at 1')
def step_impl(context):
    response = requests.get(f"{context.base_url}/")
    assert '<span id="counter">1</span>' in response.text

@then('the counter should be at 2')
def step_impl(context):
    response = requests.get(f"{context.base_url}/")
    assert '<span id="counter">2</span>' in response.text

@when('a user clicks the "Reset" button')
def step_impl(context):
    response = requests.post(f"{context.base_url}/reset")
    assert response.status_code == 200

@then('the counter should be at 0')
def step_impl(context):
    response = requests.get(f"{context.base_url}/")
    assert '<span id="counter">0</span>' in response.text