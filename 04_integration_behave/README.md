# Integration testing using BDD with Behave

In this exercise, we will implement integration testing using Behavior-Driven Development (BDD) principles with the `behave` framework and a minimal Flask application. Our main goal is to specify system behavior from an outside stakeholder perspective using natural language Gherkin feature files and implement the underlying step definitions that execute integration calls against the app.

First of all, examine the provided Flask hit counter application in `app.py`. You can run the app and access it through your web browser to understand its workflow and controls.

```bash
python app.py
```

## Step 0: Make sure dependencies are installed

Ensure `behave` and `requests` are installed in your environment. Uncomment `behave` and `requests` in `requirements.txt`, and then run pip in your virtual environment.

```bash
pip install -r requirements.txt
```

## Step 1: Create the Feature File

We will create a `.feature` file to describe the application's behavior in a human-readable format.

Your Tasks:
1. Create a directory named `features` if it does not already exist.
2. Inside the `features` folder, create a new file named `counter.feature`.
3. Define the `Feature: Hit Counter` using the standard user story template:
   ```gherkin
   Feature: <Title>

     As a <role>
     I want <functionality>
     So that <benefit>
   ```
4. Define a scenario named `The counter goes up when the button is clicked`:
   - Set up the initial state: `Given the counter is reset`.
   - Simulate user action: `When a user clicks the "Hit" button`.
   - Verify the state: `Then the counter should be at 1`.
   - Click the button a second time and assert that the counter reaches 2.

## Step 2: Write the Step Definitions

We will implement the Python step definitions that maps each line in our Gherkin file to executable HTTP calls against the Flask application.

Your Tasks:
1. Create a subfolder named `steps` inside the `features` directory.
2. Create a new Python file named `web_steps.py` inside `features/steps/`.
3. Import the required decorators and libraries: `from behave import given, when, then` and `import requests`.
4. Implement the `@given('the counter is reset')` step definition:
   - Send a `POST` request to `f"{context.base_url}/reset"`.
     ```python
     requests.post("YOUR_URL_HERE")
     ```
   - Assert that the response status code is `200`.
5. Implement the `@when('a user clicks the "Hit" button')` step definition:
   - Send a `POST` request to `f"{context.base_url}/hit"`.
   - Assert that the response status code is `200`.
6. Implement the `@then('the counter should be at 1')` step definition:
   - Send a `GET` request to `f"{context.base_url}/"`.
     ```python
     requests.get("YOUR_URL_HERE")
     ```
   - Assert that `f"<span id=\"counter\">1</span>"` is contained within `response.text`.
7. Implement the `@then('the counter should be at 2')` step definition:
   - Send a `GET` request to `f"{context.base_url}/"`.
   - Assert that `f"<span id=\"counter\">2</span>"` is contained within `response.text`.

## Step 3: Run the Test Suite

We will start our Flask web server and execute `behave` to verify that our initial scenario passes.

Your Tasks:
1. Run the Flask application from your project root in your primary terminal:
   ```bash
   python app.py
   ```
2. Open a **second terminal**, navigate to the project root, and execute the test runner:
   ```bash
   behave
   ```
3. Verify that 1 feature, 1 scenario, and 5 steps pass successfully.

## Step 4: Add a Scenario for the Reset Action

We will expand our behavioral specifications by writing a second scenario to verify the reset button functionality.

Your Tasks:
1. Open `features/counter.feature`.
2. Add a second scenario named `The counter resets to zero when the reset button is clicked`.
3. In this scenario:
   - Start with a reset counter.
   - Click the "Hit" button twice to increment the counter to 2.
   - Simulate clicking the reset button: `When a user clicks the "Reset" button`.
   - Verify that the counter returns to 0: `Then the counter should be at 0`.
4. Open `features/steps/web_steps.py` and implement the missing step definition for `@when('a user clicks the "Reset" button')`:
   - Send a `POST` request to `f"{context.base_url}/reset"`.
   - Assert that the response status code is `200`.
5. Implement the `@then('the counter should be at 0')` step definition:
   - Send a `GET` request to `f"{context.base_url}/"`.
   - Assert that `f"<span id=\"counter\">0</span>"` is contained within `response.text`.
6. Run `behave` in your second terminal:
   ```bash
   behave
   ```
7. Confirm that both scenarios pass completely.
