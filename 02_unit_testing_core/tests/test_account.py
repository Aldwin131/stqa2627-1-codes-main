"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

from random import randrange
from models.account import Account, DataValidationError


ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """Connect to database and load test data once before all tests"""

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database after running all tests"""

    def setUp(self):
        """Truncate tables before each test to guarantee isolation"""
        db.session.query(Account).delete()
        db.session.commit()
        # Memilih indeks acak dari ACCOUNT_DATA untuk pengujian dinamis
        self.rand = randrange(0, len(ACCOUNT_DATA))

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    #no1

    def test_repr(self):
        """ Test the representation of an account """
        account = Account()
        account.name = "Foo"
        self.assertEqual(str(account), "<Account 'Foo'>")


    #no2

    @classmethod
    def setUpClass(cls):
        """Connect to database and load test data once before all tests"""
        db.create_all()
        global ACCOUNT_DATA
        with open("tests/fixtures/account_data.json") as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database after running all tests"""
        db.session.remove()


    #no4

    def test_create_account(self):
        """ Test create an account """
        account = Account(**ACCOUNT_DATA[0])
        account.create()
        self.assertEqual(len(Account.all()), 1)


    #no6

    def test_create_all_accounts(self):
        """ Test creating all accounts from fixture """
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        
        # Memastikan jumlah record di database sama dengan jumlah data di JSON
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))


    #no7
    
    def test_to_dict(self):
        """ Test serializing an account to a dictionary """
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.create()
        account_dict = account.to_dict()
        self.assertEqual(account_dict["name"], data["name"])
        self.assertEqual(account_dict["email"], data["email"])

    def test_from_dict(self):
        """ Test deserializing an account from a dictionary """
        data = ACCOUNT_DATA[self.rand]
        account = Account()
        account.from_dict(data)
        self.assertEqual(account.name, data["name"])
        self.assertEqual(account.email, data["email"])

    def test_update_an_account(self):
        """ Test updating an account """
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.create()
        
        account.name = "Updated Name"
        account.update()
        
        found = Account.find(account.id)
        self.assertEqual(found.name, "Updated Name")

    def test_invalid_id_on_update(self):
        """ Test updating an account with invalid ID raises DataValidationError """
        account = Account()
        account.id = None
        account.name = "Foo"
        with self.assertRaises(DataValidationError):
            account.update()

    def test_delete_an_account(self):
        """ Test deleting an account """
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.create()
        
        self.assertEqual(len(Account.all()), 1)
        account.delete()
        self.assertEqual(len(Account.all()), 0)
