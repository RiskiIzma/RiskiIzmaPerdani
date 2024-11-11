# Fungsi untuk menghitung luas lingkaran

def hitung_luas_lingkaran(jari_jari):
 # Import konstanta pi dari modul math
    import math
# Menghitung luas lingkaran menggunakan rumus π * r^2
    luas = math.pi * jari_jari**2
    return luas

# Input dari pengguna untuk jari-jari lingkaran
jari_jari = float(input("Masukkan Nilai r: "))

# Memanggil fungsi untuk menghitung luas dan menampilkan hasil
luas = hitung_luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")