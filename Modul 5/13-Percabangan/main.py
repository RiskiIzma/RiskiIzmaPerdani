# Percabangan
# Percabangan 1 kondisi

# Struktur percabangan
"""
1.if nya
2.kondisinya,statement yang harus terpenuhiagar aksi dijalankan
3.aksinya
"""

nama = input("Masukan nama anda!")
# Percabangan
# if <kondisi> : <aksi>
if nama == "Riski" : print("Selamat Datang")
print("Terima Kasih") # bukan aksi

if nama == "Riski":
    print("Selamat Datang") # Aksi
    print("Selamat Belajar")  # Aksi
print("Terima Kasih") # bukan aksi

# Percabangan dengan else statement
if nama == "Riski":
    print("Selamat Datang")
else:
    print("Anda Bukan Riski")

print("Program Berakhir")