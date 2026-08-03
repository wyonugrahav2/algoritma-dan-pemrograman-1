import random

class GuessingGame:
    def __init__(self, min_val: int = 1, max_val: int = 10):
        self.min_val = min_val
        self.max_val = max_val
        self.secret_number = random.randint(min_val, max_val)
        self.attempts = 0
        self.is_over = False

    def check_guess(self, guess: int) -> str:
        """Mengecek tebakan pemain dan mengembalikan status umpan balik."""
        self.attempts += 1
        
        if guess < self.secret_number:
            return "Terlalu kecil! 📉"
        elif guess > self.secret_number:
            return "Terlalu besar! 📈"
        else:
            self.is_over = True
            return "Tebakan benar! 🎉"