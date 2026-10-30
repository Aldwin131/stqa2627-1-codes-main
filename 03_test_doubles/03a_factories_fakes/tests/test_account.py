"""
Test Cases TestAccountModel
"""

from unittest import TestCase
from models import db
from models.account import Account, DataValidationError

from tests.factories import AccountFactory


class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        accounts = AccountFactory.create_batch(10)
        for account in accounts:
            account.create()
        
        self.assertEqual(len(Account.all()), 10)

    def test_create_an_account(self):
        """ Test Account creation using known data """
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_repr(self):
        """Test the representation of an account"""
        account = Account()
        account.name = "Foo"
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_to_dict(self):
        """ Test account to dict """
        account = AccountFactory()
        account.create()
        account_dict = account.to_dict()
        self.assertEqual(account_dict["name"], account.name)
        self.assertEqual(account_dict["email"], account.email)

    def test_from_dict(self):
        """ Test account from dict """
        # Bikin data palsu menggunakan factory, lalu jadikan dictionary
        account = AccountFactory()
        account_dict = account.to_dict()
        
        # Buat akun kosong dan isi datanya dari dictionary tadi
        new_account = Account()
        new_account.from_dict(account_dict)
        
        # Pastikan data yang masuk sesuai
        self.assertEqual(new_account.name, account.name)
        self.assertEqual(new_account.email, account.email)

    def test_update_an_account(self):
        """ Test Account update using known data """
        # Buat dan simpan akun palsu ke database
        account = AccountFactory()
        account.create()
        
        # Ubah nama akun tersebut
        account.name = "Updated Name"
        account.update()
        
        # Cari kembali akun tersebut di database dan pastikan namanya sudah berubah
        found = Account.find(account.id)
        self.assertEqual(found.name, "Updated Name")

    def test_invalid_id_on_update(self):
        """ Test invalid ID update """
        """ Test invalid ID on update raises DataValidationError """
        # Buat akun menggunakan factory
        account = AccountFactory()
        
        # Hapus ID-nya agar menjadi tidak valid
        account.id = None
        
        # Pastikan saat di-update akan memunculkan error DataValidationError
        with self.assertRaises(DataValidationError):
            account.update()

    def test_delete_an_account(self):
        """ Test Account delete using known data """
        # Buat akun palsu dan simpan ke database
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1)
        
        # Hapus akun tersebut dan pastikan database kembali kosong
        account.delete()
        self.assertEqual(len(Account.all()), 0)

