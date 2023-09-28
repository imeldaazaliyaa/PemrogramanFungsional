class Peserta:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama
        self.nilai = 0
    
    def input_nilai(self, nilai):
        self.nilai = nilai
    
    def cek_hasil(self):
        if self.nilai >= 75:
            return "Lolos"
        else:
            return "Tidak Lolos"

class Admin:
    def __init__(self):
        self.peserta_list = []
    
    def tambah_peserta(self, id, nama):
        peserta = Peserta(id, nama)
        self.peserta_list.append(peserta)
    
    def edit_nilai_peserta(self, id, nilai):
        peserta = next((p for p in self.peserta_list if p.id == id), None)
        if peserta:
            peserta.input_nilai(nilai)
        else:
            print("ID Peserta tidak ditemukan!")

    def tampilkan_data_peserta(self):
        print("=========================================================")
        print("|   ID   |  Nama  |   Nilai   |       Hasil Akhir       |")
        print("=========================================================")
        for peserta in self.peserta_list:
            print(f"|   {peserta.id}    | {peserta.nama}|     {peserta.nilai}      |      {peserta.cek_hasil()}      |")
        print("=========================================================")

def main():
    admin = Admin()

    while True:
        print("\nMenu:")
        print("1. Tambah Peserta")
        print("2. Edit Nilai Peserta")
        print("3. Tampilkan Data Peserta")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            id = int(input("Masukkan ID peserta: "))
            nama = input("Masukkan nama peserta: ")
            admin.tambah_peserta(id, nama)
        elif pilihan == "2":
            id = int(input("Masukkan ID peserta: "))
            nilai = int(input("Masukkan nilai peserta: "))
            admin.edit_nilai_peserta(id, nilai)
        elif pilihan == "3":
            admin.tampilkan_data_peserta()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
