import unittest
from src.logic.math_cases import calculate_factorial, generate_power_table
from src.logic.guessing_game import GuessingGame


class TestM6Logic(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

    def test_power_table(self):
        table = generate_power_table(3)
        self.assertEqual(len(table), 3)
        self.assertEqual(table[1]["kuadrat"], 4)
        self.assertEqual(table[2]["kubik"], 27)

    def test_guessing_game(self):
        game = GuessingGame(1, 10)
        game.secret_number = 5  # Mock angka rahasia

        self.assertEqual(game.check_guess(3), "Terlalu kecil! 📉")
        self.assertEqual(game.check_guess(8), "Terlalu besar! 📈")
        self.assertEqual(game.check_guess(5), "Tebakan benar! 🎉")
        self.assertTrue(game.is_over)


if __name__ == "__main__":
    unittest.main()