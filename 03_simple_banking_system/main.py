import sys
import os

# Menambahkan path src agar modul lokal bisa di-import dengan rapi
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from utils.file_handler import load_accounts, save_accounts
from logic.auth import verify_pin
from logic.transaction import check_balance, deposit, withdraw
from ui.menu import show_welcome, show_menu


def main():
    show_welcome()
    accounts = load_accounts()

    if not accounts:
        print("Data akun tidak ditemukan atau berkas JSON kosong!")
        return

    # 1. Autentikasi No Rekening & PIN
    account_number = input("Masukkan Nomor Rekening : ")
    account = next((acc for acc in accounts if acc["account_number"] == account_number), None)

    if not account:
        print("Nomor rekening tidak terdaftar!")
        return

    pin_input = input("Masukkan PIN Anda           : ")
    if not verify_pin(pin_input, account):
        print("PIN salah! Akses ditolak.")
        return

    # 2. Loop Menu Utama
    while True:
        show_menu(account["name"])
        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            balance = check_balance(account)
            print(f"\n>> Saldo Anda saat ini: Rp {balance:,}")

        elif choice == "2":
            try:
                amount = int(input("\nMasukkan nominal setor: Rp "))
                success, msg = deposit(account, amount)
                print(f">> {msg}")
                if success:
                    save_accounts(accounts)
            except ValueError:
                print(">> Input harus berupa angka!")

        elif choice == "3":
            try:
                amount = int(input("\nMasukkan nominal tarik: Rp "))
                success, msg = withdraw(account, amount)
                print(f">> {msg}")
                if success:
                    save_accounts(accounts)
            except ValueError:
                print(">> Input harus berupa angka!")

        elif choice == "4":
            print("\nTerima kasih telah menggunakan layanan ATM Simple!")
            break
        else:
            print(">> Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()