# meminta input total belanja dari pengguna
total_belanja = float(input("Masukan Total Belanja Anda(dalam Rp): "))

# menentukan hadiah berdasarkan total belanja
if total_belanja >= 5000000:
    hadiah = "mouse dan keyboard"
else:
    hadiah = "gantungan kunci"

# menampilkan hasil
print(f"Anda mendapatkan hadiah: {hadiah}")
print("input tidak valid.harap masukan angka dengan benar")
print("Belanja anda kurang dari Rp 5000000")