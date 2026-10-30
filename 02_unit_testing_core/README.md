# Unit Testing Core Mechanics: Assertions, Fixtures, and Coverage

In this exercise, we will implement unit tests for a database-backed `Account` model using `PyUnit` (`unittest`), but with a `pytest` runner. Our main goal is to understand test lifecycles (class-level vs. test-level fixtures), write meaningful assertions, and achieve high test coverage.

First of all, examine the provided application code in `models/account.py` and ensure your `pytest.ini` configuration file is properly set up. The configurations in `pytest.ini` let us run `pytest` without typing all the options every single time.

## Step 1: Writing Your First Assertion

Begin by creating a standalone unit test that validates object state in memory without needing database persistence. This tests the function `__repr__` in the `Account` class.

Your Tasks:
1. Open the test file (e.g., `tests/test_account.py`).
2. Implement a test method `test_repr`.
3. Instantiate an `Account` object, set `account.name = "Foo"`, and use `self.assertEqual` to verify that `str(account)` evaluates to `"<Account 'Foo'>"`.
4. Run pytest to see your first assertion pass.
   ```bash
   pytest
   ```

## Step 2: Setting Up Class-Level Fixtures

Set up class-level fixtures (`setUpClass` and `tearDownClass`) to manage database connections and load shared test data into memory once for the entire test suite.

Your Tasks:
1. Open the test file (e.g., `tests/test_account.py`).
2. Implement `setUpClass`:
   - Initialize the database tables using `db.create_all()`.
   - Load fixture data from `tests/fixtures/account_data.json` into a global variable `ACCOUNT_DATA`.
3. Implement `tearDownClass`:
   - Disconnect and clean up the database session using `db.session.remove()`.

## Step 3: Initial Baseline and Coverage Check

Run the test runner to observe the baseline coverage before writing any test cases.

Your Tasks:
1. Add the following options to the configurations in the `pytest.ini` file. The `cov` option specifies which codes are calculated for coverage, and the `cov-report=term-missing` option instructs pytest to print which line numbers of your application code were executed or missed.
   ```bash
   addopts = -v --cov=models --cov-report=term-missing
   ```
2. Run pytest.
   ```bash
   pytest
   ```
3. Observe the terminal report. Many lines in `models/account.py` will be flagged as unvisited because no test cases have executed yet.

## Step 4: Writing Your First Test Case

Create a test case to verify creating a single account and inspect what happens when tests alter the database state.

Your Tasks:
1. Implement a test method `test_create_account` that instantiates an `Account` using the first entry in `ACCOUNT_DATA`, calls `account.create()`, and asserts that the total count of accounts in the database equals 1.
2. Run pytest.
   ```bash
   pytest
   ```
3. Run the exact same command a second time. Notice that the test fails because leftover database state from the first run causes the count assertion to fail.

## Step 5: Adding Test-Level Fixtures

Implement a `setUp` fixture that runs before every individual test method to isolate tests and ensure a clean database state.

Your Tasks:
1. Implement the `setUp` method to truncate the table by calling `db.session.query(Account).delete()`.
2. Re-run the tests.
   ```bash
   pytest
   ```
3. Run the command repeatedly to confirm that the test passes consistently without cross-test contamination.

## Step 6: Testing Bulk Operations

Add a test case that creates all accounts from the loaded JSON data to verify batch creation behavior.

Your Tasks:
1. Implement `test_create_all_accounts` by looping over each item in `ACCOUNT_DATA`, creating an account, and asserting that the total record count matches the length of `ACCOUNT_DATA`.
2. Run the tests.
   ```bash
   pytest
   ```
3. Observe the increase in code coverage in the output report.

## Step 7: Raising Coverage with Assertions and Edge Cases

Implement comprehensive tests for string representation, serialization, updates, error handling, and deletion to maximize branch and line coverage.

Your Tasks:
1. Import necessary helpers:
   - `from random import randrange`
   - `from models.account import DataValidationError`
2. Update `setUp` to pick a random index (`self.rand = randrange(0, len(ACCOUNT_DATA))`) for parameterized sampling.
3. Implement `test_to_dict` and `test_from_dict` to validate serialization/deserialization.
4. Implement `test_update_an_account` and `test_invalid_id_on_update` to test updates and error handling (`assertRaises`).
5. Implement `test_delete_an_account` to verify record deletion.
6. Run the tests and verify that missing lines in `models/account.py` approach 0:
   ```bash
   pytest
   ```
