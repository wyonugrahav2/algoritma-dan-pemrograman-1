import unittest
import sys
import os

# Menambahkan src ke sys.path untuk impor modul
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from logic.transaction import deposit, withdraw


class TestTransactionLogic(unittest.TestCase):

    def setUp(self):
        """Menyiapkan data akun dummy sebelum tiap tes dijalankan."""
        self.account = {
            "account_number": "9999",
            "pin": "0000",
            "name": "Test User",
            "balance": 100000
        }

    def test_deposit_success(self):
        success, msg = deposit(self.account, 50000)
        self.assertTrue(success)
        self.assertEqual(self.account["balance"], 150000)

    def test_withdraw_success(self):
        success, msg = withdraw(self.account, 40000)
        self.assertTrue(success)
        self.assertEqual(self.account["balance"], 60000)

    def test_withdraw_insufficient_funds(self):
        success, msg = withdraw(self.account, 200000)
        self.assertFalse(success)
        self.assertEqual(self.account["balance"], 100000)  # Saldo tidak boleh berkurang


if __name__ == "__main__":
    unittest.main()