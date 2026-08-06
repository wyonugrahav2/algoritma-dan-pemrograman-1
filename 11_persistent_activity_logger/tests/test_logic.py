import unittest

from src.logic.log_entry import (
    format_log_entry,
    matches_keyword,
    parse_log_entry,
    validate_activity,
)


class TestM11Logic(unittest.TestCase):

    def test_validate_activity(self):
        self.assertEqual(validate_activity("  Belajar Python  "), "Belajar Python")
        with self.assertRaises(ValueError):
            validate_activity("   ")
        with self.assertRaises(ValueError):
            validate_activity("Aktivitas | Tidak Valid")

    def test_format_and_parse_log_entry(self):
        line = format_log_entry("Belajar Python", "Modul File I/O")
        self.assertTrue(line.endswith("\n"))

        entry = parse_log_entry(line)
        self.assertEqual(entry["aktivitas"], "Belajar Python")
        self.assertEqual(entry["keterangan"], "Modul File I/O")
        self.assertTrue(len(entry["timestamp"]) > 0)

    def test_format_log_entry_default_keterangan(self):
        line = format_log_entry("Push ke GitHub", "")
        entry = parse_log_entry(line)
        self.assertEqual(entry["keterangan"], "-")

    def test_parse_log_entry_invalid_format(self):
        with self.assertRaises(ValueError):
            parse_log_entry("format baris tidak sesuai")

    def test_matches_keyword(self):
        entry = {"aktivitas": "Belajar Python", "keterangan": "Modul File I/O"}
        self.assertTrue(matches_keyword(entry, "python"))
        self.assertTrue(matches_keyword(entry, "FILE"))
        self.assertFalse(matches_keyword(entry, "javascript"))


if __name__ == "__main__":
    unittest.main()
