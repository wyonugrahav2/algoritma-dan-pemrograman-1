"""
Pengujian Unit (Unit Test) Modul Autentikasi Login
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logic.auth import authenticate_user


class TestAuthLogic(unittest.TestCase):

    def setUp(self):
        self.mock_db = {
            "users": [
                {"username": "admin", "password": "python", "is_locked": False}
            ]
        }

    def test_successful_login(self):
        is_success, msg = authenticate_user("admin", "python", self.mock_db)
        self.assertTrue(is_success)
        self.assertIn("berhasil", msg.lower())

    def test_failed_login(self):
        is_success, msg = authenticate_user("admin", "wrongpass", self.mock_db)
        self.assertFalse(is_success)
        self.assertIn("salah", msg.lower())


if __name__ == "__main__":
    unittest.main()