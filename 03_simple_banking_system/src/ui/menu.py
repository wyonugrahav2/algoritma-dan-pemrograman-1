def show_welcome():
    print("\n" + "=" * 40)
    print("      SELAMAT DATANG DI ATM SIMPLE      ")
    print("=" * 40)


def show_menu(user_name):
    print(f"\nHalo, {user_name}!")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Keluar")
    print("-" * 40)