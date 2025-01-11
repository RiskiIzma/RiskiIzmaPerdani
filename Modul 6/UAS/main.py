class Pegawai:
    def __init__(self, nama, gaji_pokok, durasi_lembur):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
        self.durasi_lembur = durasi_lembur

    def hitung_gaji_bersih(self):
        pass

    def tampilkan_info(self):
        pass

class PegawaiTetap(Pegawai):
    def __init__(self, nama, gaji_pokok, durasi_lembur):
        super().__init__(nama, gaji_pokok, durasi_lembur)

    def hitung_tunjangan(self):
        return 0.7 * self.gaji_pokok

    def hitung_lembur(self):
        return self.durasi_lembur * (0.1 * self.gaji_pokok)

    def hitung_gaji_bersih(self):
        return self.gaji_pokok + self.hitung_tunjangan() + self.hitung_lembur()

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji Pokok: {self.gaji_pokok}")
        print(f"Tunjangan: {self.hitung_tunjangan()}")
        print(f"Durasi Lembur: {self.durasi_lembur} jam")
        print(f"Gaji Bersih: {self.hitung_gaji_bersih()}")

class PegawaiTidakTetap(Pegawai):
    def __init__(self, nama, gaji_pokok, durasi_lembur):
        super().__init__(nama, gaji_pokok, durasi_lembur)

    def hitung_lembur(self):
        return self.durasi_lembur * (0.05 * self.gaji_pokok)

    def hitung_gaji_bersih(self):
        return self.gaji_pokok + self.hitung_lembur()

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji Pokok: {self.gaji_pokok}")
        print(f"Tunjangan: Tidak Ada")
        print(f"Durasi Lembur: {self.durasi_lembur} jam")
        print(f"Gaji Bersih: {self.hitung_gaji_bersih()}")

# Input Manual dari Pengguna
print("Masukkan data pegawai:")
nama = input("Nama: ")
gaji_pokok = float(input("Gaji Pokok: "))
durasi_lembur = int(input("Durasi Lembur (jam): "))
status = input("Status Pegawai (Tetap/Tidak Tetap): ").lower()

if status == "tetap":
    pegawai = PegawaiTetap(nama, gaji_pokok, durasi_lembur)
elif status == "tidak tetap":
    pegawai = PegawaiTidakTetap(nama, gaji_pokok, durasi_lembur)
else:
    print("Status pegawai tidak valid.")
    exit()

print("\nInformasi Pegawai:")
pegawai.tampilkan_info()