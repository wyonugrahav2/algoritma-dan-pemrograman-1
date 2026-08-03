from src.logic.guessing_game import GuessingGame
from src.logic.math_cases import calculate_factorial, generate_power_table
from src.utils.score_tracker import load_history, save_game_result


def show_math_menu():
    print("\n--- 🔢 Kalkulator & Tabel Matematika ---")
    print("1. Hitung Faktorial (n!)")
    print("2. Tampilkan Tabel Kuadrat & Kubik")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        try:
            n = int(input("Masukkan angka positif: "))
            hasil = calculate_factorial(n)
            print(f"✨ Hasil {n}! adalah {hasil}")
        except ValueError as e:
            print(f"❌ Input tidak valid: {e}")
    elif pilihan == "2":
        try:
            limit = int(
                input("Masukkan batas angka (default 5): ") or "5"
            )
            data = generate_power_table(limit)
            print("\nBil\tKuadrat\tKubik")
            print("-" * 25)
            for row in data:
                print(
                    f"{row['bilangan']}\t{row['kuadrat']}\t\t{row['kubik']}"
                )
        except ValueError:
            print("❌ Harap masukkan angka yang valid!")


def play_game_menu():
    print("\n--- 🎮 Game Tebak Angka (1 - 10) ---")
    nama = input("Masukkan nama pemain: ").strip() or "Player"
    game = GuessingGame(1, 10)

    while not game.is_over:
        try:
            tebakan = int(input("Tebak angka (1-10): "))
            feedback = game.check_guess(tebakan)
            print(feedback)
        except ValueError:
            print("❌ Harap masukkan angka!")

    print(f"🎉 Selamat {nama}! Kamu berhasil menebak dalam {game.attempts} kali percobaan.")
    save_game_result(nama, game.attempts, game.secret_number)


def show_history_menu():
    print("\n--- 📜 Riwayat Skor Game ---")
    history = load_history()
    if not history:
        print("Belum ada riwayat permainan.")
        return

    print("Nama\t\tPercobaan\tAngka Rahasia")
    print("-" * 45)
    for record in history:
        print(
            f"{record['player_name']}\t\t{record['attempts']}\t\t{record['secret_number']}"
        )