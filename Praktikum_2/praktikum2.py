# ========================================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 1 - Membaca dan Menulis File Teks
# ========================================================

# Variabel untuk menyimpan nama file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} # Inisialisasi data dictionary
    with open("data_mahasiswa.txt", "r", encoding= "utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan spasi
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} #masukan dalam dictionary
    return data_dict

buka_data = baca_data(nama_file) #memanggil fungsi data dan menyimpan dalam variabel
print("jumlah data mahasiswa:", len(buka_data)) #menampilkan jumlah data mahasiswa


# ========================================================
# Praktikum 2 - Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 2 - Membuat fungsi menampilkan dat
# ========================================================

def tampilkan_data(data_dict):
    # Menampilkan header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' : <10} | {'NAMA': <12} | {'NILAI':5}")
    
    print("-" * 32) #membuat garis
    
    #menampilkan isi data mahasiswa
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) :<5}")

#tampilkan_data(buka_data) #memanggil fungsi tampilkan data

# ========================================================
# Praktikum 2 - Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3 - mencari data mahasiswa berdasarkan NIM
# ========================================================

# membuat fungsi pencarian data 
def cari_data(data_dict):
    # pencarian data berdasarkan NIM sebagai key dalam dictionary
    # membuat input nim mahasiswa yang akan di cari
    nim_cari = input("\nMasukkan NIM mahasiswa yang dicari: ").strip()


    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("=== DATA MAHASISWA DITEMUKAN ===")
        print(f"NIM  : {nim_cari}")
        print(f"NAMA : {nama}")
        print(f"NILAI: {nilai}")
    else:
        print("Data mahasiswa dengan NIM tersebut tidak ditemukan.")



#cari_data(buka_data) #memanggil fungsi cari data

# ========================================================
# Praktikum 2 - Konsep ADT dan File Handling (STUDI KASUS
# Latihan 4 - Membuat fungsi update  mahasiswa
# ========================================================

# membuat fungsi update mahasiswa
def ubah_data(data_dict):

    #awali dulu dengan input nim mahasiswa yang akan di ubah
    nim = input("\nMasukkan NIM mahasiswa yang ingin di ubah nilai nya: ").strip()
    if nim not in data_dict:
        print("Data mahasiswa dengan NIM tersebut tidak ditemukan.")
        return data_dict
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: "))
        if nilai_baru < 0 or nilai_baru > 100:
            print("Nilai harus antara 0-100.")
            return data_dict
    except ValueError:
        print("Input nilai tidak valid. Harus berupa angka antara 0-100.")
        return data_dict
    
    nilai_lama = data_dict[nim]["nilai"]
    
    data_dict[nim]["nilai"] = nilai_baru
    print("=== DATA MAHASISWA BERHASIL DIUBAH ===")
    print(f"NIM  : {nim}")
    print(f"NAMA : {data_dict[nim]['nama']}")
    print(f"NILAI: {nilai_lama} -> {nilai_baru}")
    return data_dict
#ubah_data(buka_data) #memanggil fungsi ubah data

# ========================================================
# Praktikum 2 - Konsep ADT dan File Handling (STUDI KAS
# Latihan 5 - Menyimpan perubahan data ke file
# ========================================================

#membuat fungsi simpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8")as file:
        for nim in data_dict:
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("\nData berhasil disimpan ke file.")
#simpan_data(nama_file, buka_data) #memanggil fungsi simpan data

# ========================================================
# Praktikum 2 - Konsep ADT dan File Handling (STUDI KASUS
# Latihan 6 - Membuat menu interaktif
# =======================================================

def main():
    #load data otomatis saat program di mulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            buka_data = ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data telah disimpan.")
        elif pilihan == "5":    
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()
        





