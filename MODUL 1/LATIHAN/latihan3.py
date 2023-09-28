# Sistem Penilaian Akhir Mahasiswa

# Fungsi untuk menghitung nilai akhir mahasiswa berdasarkan nilai UTS dan UAS
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_uts, nilai_uas = nilai['uts'], nilai['uas']
        nilai_akhir = hitung_nilai_akhir(nilai_uts, nilai_uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menambahkan data mahasiswa ke dalam dictionary data_mahasiswa
def tambahkan_mahasiswa(data_mahasiswa, nama, uts, uas):
    data_mahasiswa[nama] = {'uts': uts, 'uas': uas}

# Fungsi utama
def main():
    data_mahasiswa = {}  # Inisialisasi dictionary data_mahasiswa

    # Tambahkan data mahasiswa ke dalam dictionary
    tambahkan_mahasiswa(data_mahasiswa, 'Mahasiswa 1', 80, 90)
    tambahkan_mahasiswa(data_mahasiswa, 'Mahasiswa 2', 75, 85)
    tambahkan_mahasiswa(data_mahasiswa, 'Mahasiswa 3', 90, 95)

    # Menghitung nilai akhir semua mahasiswa
    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    # Menampilkan hasil nilai akhir mahasiswa
    tampilkan_nilai_akhir(data_nilai_akhir)

# Fungsi untuk menampilkan nilai akhir mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

if __name__ == "__main__":
    main()
