import unittest

from src.logic.contact_entry import (
    format_contact_line,
    matches_keyword,
    parse_contact_line,
    validate_contact,
)


class TestM12Logic(unittest.TestCase):

    def test_validate_contact(self):
        nama, telepon, email = validate_contact("  Andi  ", " 08123456789 ", " andi@mail.com ")
        self.assertEqual(nama, "Andi")
        self.assertEqual(telepon, "08123456789")
        self.assertEqual(email, "andi@mail.com")

        with self.assertRaises(ValueError):
            validate_contact("", "08123456789", "")
        with self.assertRaises(ValueError):
            validate_contact("Andi", "", "")
        with self.assertRaises(ValueError):
            validate_contact("Andi", "08xx-abc", "")
        with self.assertRaises(ValueError):
            validate_contact("Andi,Budi", "08123456789", "")

    def test_validate_contact_default_email(self):
        _, _, email = validate_contact("Budi", "0811111111", "")
        self.assertEqual(email, "-")

    def test_format_and_parse_contact_line(self):
        line = format_contact_line("Andi", "08123456789", "andi@mail.com")
        self.assertEqual(line, "Andi,08123456789,andi@mail.com\n")

        contact = parse_contact_line(line)
        self.assertEqual(contact["nama"], "Andi")
        self.assertEqual(contact["telepon"], "08123456789")
        self.assertEqual(contact["email"], "andi@mail.com")

    def test_parse_contact_line_invalid_format(self):
        with self.assertRaises(ValueError):
            parse_contact_line("format,tidak,sesuai,banget")

    def test_matches_keyword(self):
        contact = {"nama": "Andi", "telepon": "08123456789", "email": "andi@mail.com"}
        self.assertTrue(matches_keyword(contact, "andi"))
        self.assertTrue(matches_keyword(contact, "0812"))
        self.assertFalse(matches_keyword(contact, "budi"))


if __name__ == "__main__":
    unittest.main()
