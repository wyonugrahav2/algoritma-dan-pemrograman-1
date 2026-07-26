"""
Modul Autentikasi Login (Pertemuan 4)
Menangani mekanisme login pengguna dengan pembatasan percobaan (Max 3x)
menggunakan struktur kontrol perulangan while.
"""

def authenticate_user(input_username, input_password, user_db):
    """
    Memvalidasi kredensial pengguna terhadap basis data JSON.
    """
    for user in user_db.get("users", []):
        if user["username"] == input_username and user["password"] == input_password:
            return True, "Login berhasil! Selamat datang."
    
    return False, "Username atau password salah!"


def run_login_simulation(user_db, max_attempts=3):
    """
    Simulasi perulangan login dengan batas maksimal percobaan (while loop).
    """
    attempts = 0
    
    print("\n" + "="*40)
    print("🔐 SIMULASI LOGIN SYSTEM (MAX 3 ATTEMPTS)")
    print("="*40)

    while attempts < max_attempts:
        attempts += 1
        print(f"\n--- Percobaan ke-{attempts} dari {max_attempts} ---")
        
        username = input("Masukkan Username: ").strip()
        password = input("Masukkan Password: ").strip()

        is_success, message = authenticate_user(username, password, user_db)

        if is_success:
            print(f"✅ {message}")
            return True

        print(f"❌ {message}")
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"⚠️ Sisa percobaan Anda: {remaining}")
        else:
            print("🔒 Akses ditolak! Akun Anda terkunci karena salah 3 kali.")

    return False