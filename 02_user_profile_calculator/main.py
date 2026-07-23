"""
================================================================
My CLI Dashboard
Modul 02 - User Profile & Health/Study Calculator
Pertemuan 2 (M2): Variabel, Tipe Data, Input & Output
================================================================
Materi yang digunakan:
- Variabel & Tipe Data Dasar (int, float, str, bool)
- Fungsi input() dan print()
- Konversi Tipe Data (Type Casting)
Tidak menggunakan: if-else bercabang, loop, atau fungsi/class kustom.
================================================================
"""

# ----------------------------------------------------------------
# BAGIAN 1: INPUT DATA DIRI MAHASISWA
# input() selalu menghasilkan tipe data str, sehingga variabel
# yang butuh angka harus dikonversi (type casting) memakai int()
# atau float().
# ----------------------------------------------------------------

nama = input("Masukkan Nama Lengkap  : ")              # str, tidak perlu konversi
npm = input("Masukkan NPM           : ")                # str, NPM tetap teks (bisa ada huruf/kode kampus)
jurusan = input("Masukkan Jurusan       : ")            # str

umur = int(input("Masukkan Umur (tahun)  : "))          # str -> int
tinggi_cm = float(input("Masukkan Tinggi Badan (cm): "))  # str -> float
berat_kg = float(input("Masukkan Berat Badan (kg) : "))   # str -> float

jam_belajar_harian = float(input("Masukkan Target Jam Belajar/Hari: "))  # str -> float

# Contoh variabel bertipe bool: status keaktifan mahasiswa.
# Percabangan if-else belum dipakai, jadi nilainya ditetapkan langsung
# sebagai penanda bahwa mahasiswa yang mengisi form berarti berstatus aktif.
status_mahasiswa_aktif = True   # tipe data bool


# ----------------------------------------------------------------
# BAGIAN 2: PENGOLAHAN DATA (ARITMATIKA DASAR + TYPE CASTING)
# ----------------------------------------------------------------

# 2.1 Perkiraan tahun lahir mahasiswa
tahun_sekarang = 2026                          # int, tahun berjalan
perkiraan_tahun_lahir = tahun_sekarang - umur  # int - int = int

# 2.2 Konversi tinggi badan dari sentimeter ke meter
tinggi_m = tinggi_cm / 100                     # float, hasil bagi tetap float

# 2.3 Perhitungan BMI (Body Mass Index) sederhana
# Rumus: berat (kg) / (tinggi (m) * tinggi (m))
bmi = berat_kg / (tinggi_m * tinggi_m)         # float

# 2.4 Estimasi total jam belajar dalam satu minggu (7 hari)
total_jam_belajar_mingguan = jam_belajar_harian * 7   # float

# 2.5 Konversi status aktif (bool) menjadi teks agar rapi saat ditampilkan
status_teks = str(status_mahasiswa_aktif)      # bool -> str ("True")


# ----------------------------------------------------------------
# BAGIAN 3: OUTPUT - SUMMARY DASHBOARD (TAMPILAN ASCII TABEL)
# ----------------------------------------------------------------

print("\n" + "=" * 52)
print("       MY CLI DASHBOARD - PROFIL MAHASISWA")
print("=" * 52)

print(f"| Nama              : {nama}")
print(f"| NPM               : {npm}")
print(f"| Jurusan           : {jurusan}")
print(f"| Umur              : {umur} tahun")
print(f"| Perkiraan Lahir   : Tahun {perkiraan_tahun_lahir}")
print(f"| Status Aktif      : {status_teks}")
print("-" * 52)

print("        RINGKASAN KESEHATAN (BMI)")
print("-" * 52)
print(f"| Tinggi Badan      : {tinggi_cm} cm ({tinggi_m} m)")
print(f"| Berat Badan       : {berat_kg} kg")
print(f"| Skor BMI          : {bmi:.2f}")
print("-" * 52)

print("        RINGKASAN TARGET BELAJAR")
print("-" * 52)
print(f"| Jam Belajar/Hari  : {jam_belajar_harian} jam")
print(f"| Jam Belajar/Minggu: {total_jam_belajar_mingguan} jam")

print("=" * 52)
print("   Terima kasih telah menggunakan My CLI Dashboard!")
print("=" * 52 + "\n")
