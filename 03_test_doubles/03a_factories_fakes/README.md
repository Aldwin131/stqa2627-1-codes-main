# Factories and Fakes

In this exercise, we will modernize our test suite by replacing static JSON fixture files with dynamic test data generation using `FactoryBoy` and `Faker`. Our main goal is to decouple test cases from hardcoded fixture data, generate realistic dynamic models on demand, and maintain clean test isolation without sacrificing 100% test coverage.

First of all, examine the provided `models/account.py` file to review the attributes of the `Account` model and verify your local testing environment before proceeding.

## Step 0: Make sure FactoryBoy is installed

Uncomment factory-boy in requirements.txt and install it.

```bash
pip install -r requirements.txt
```

## Step 1: Run tests

Before you make any changes to the code, you want to be sure that all of the test cases are passing. Otherwise, you may encounter failing test cases later and you won't know if you caused them to fail, or if they were failing before you changed anything.

Let's run `pytest` and be sure that all of the tests are passing with **100%** test coverage.

```bash
pytest
```

## Step 2: Create an AccountFactory class

In this step we will create an `AccountFactory` class.

Open the `models/account.py` file to familiarize yourself with the attributes of the `Account` class. These are the same attributes that you will need to add to the `AccountFactory` class.

Open the `tests/factories.py` file in the IDE editor.

We want to take advantage of the fact that **FactoryBoy** comes with the **Faker** class which has [Fake providers](https://faker.readthedocs.io/en/master/providers/baseprovider.html) and a number of [Fuzzy attributes](https://factoryboy.readthedocs.io/en/stable/fuzzy.html).

Here are some useful providers for the Faker class:

```
Faker("name")
Faker("email")
Faker("phone_number")
```

Here are some Fuzzy attributes you might find useful:

```
FuzzyChoice(choices=[True, False])
FuzzyDate(date(2008, 1, 1))
```

Use the **Faker** providers and **Fuzzy** attributes to create fake data for the `id`, `name`, `email`, `phone_number`, `disabled`, and `date_joined` fields by adding them to the `AccountFactory` class.

## Step 3: Update the test cases

In this step we will update the test cases to use the new `AccountFactory` that you created in the previous step.

Open the `tests/test_account.py` file. Then add the following import near the top of the file, after the other `imports`. This will import your new `AccountFactory` class from the `factories` module:

```py
from factories import AccountFactory
```

In the remaining steps, we want to change all of the referenced to `Account` to now use `AccountFactory`. We will do this one test at a time.

Let's start with the `test_create_all_accounts()` test. Remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`. Also change the code to create 10 Accounts.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 4: Update test_create_an_account()

In this step we will update the `test_create_an_account()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 5: Update test_to_dict()

In this step we will update the `test_to_dict()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 6: Update test_from_dict()

In this step we will update the `test_from_dict()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 7: Update test_update_an_account()

In this step we will update the `test_update_an_account()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 8: Update test_invalid_id_on_update()

In this step we will update the `test_invalid_id_on_update()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 9: Update test_delete_an_account()

In this step we will update the `test_delete_an_account()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `pytest` to make sure the test cases still pass.

```bash
pytest
```

## Step 10: Remove ACCOUNT_DATA references

Since we have replaced all of the instance of `ACCOUNT_DATA` with `AccountFactory`, we can clean up the code by removing all remaining references to `ACCOUNT_DATA` and also remove loading it from the json data file.

Remove line 31 from `setUp()`:

```py
self.rand = randrange(0, len(ACCOUNT_DATA))
```

Remove lines 20-22 from `setUpClass()`:

```py
global ACCOUNT_DATA
with open('tests/fixtures/account_data.json') as json_data:
    ACCOUNT_DATA = json.load(json_data)
```

You can also delete line `11` that declares `ACCOUNT_DATA`:

```py
ACCOUNT_DATA = {}   # <- delete this line
```

Finally delete line 4-5 that imports `json` and  `randrange`:

```py
import json
from random import randrange
```

Save you changes and run `pytest` one last time to make sure the test cases still pass.

```bash
pytest
```

You should see:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      0   100%
--------------------------------------------------
TOTAL                   46      0   100%
```
