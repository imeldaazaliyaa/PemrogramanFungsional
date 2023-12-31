random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]

# Inisialisasi variabel untuk menyimpan nilai int, float, dan string
int_values = {}
float_values = ()
string_values = []

# Iterasi melalui random_list untuk memisahkan nilai
for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100) % 10
        
        # Menyimpan dalam dictionary
        int_values[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        # Menambahkan float ke dalam tuple
        float_values += (item,)
    elif isinstance(item, str):
        # Menambahkan string ke dalam list
        string_values.append(item)

# Menampilkan hasil pemisahan
print("Nilai Integer (dalam bentuk dictionary):")
print(int_values)
print("\nNilai Float (dalam bentuk tuple):")
print(float_values)
print("\nNilai String (dalam bentuk list):")
print(string_values)