# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Zaky Alnadif
# NIM     : J0403251126
# Kelas   : TPL A2
# ==============================================================================
import os

# 1. FILE HANDLING & DICTIONARY
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca file teks (misalnya 'buku.txt') dan menyimpannya ke Dictionary.
    Format file yang diharapkan: kode_buku,judul,harga
    Dictionary menggunakan kode_buku sebagai key, dan dictionary lain (judul, harga) sebagai value.
    """
    database_buku = {}
    
    # Mengecek apakah file ada sebelum dibaca
    if os.path.exists(nama_file):
        with open(nama_file, 'r') as file:
            for baris in file:
                # Menghapus spasi/newline dan memisahkan berdasarkan koma
                data = baris.strip().split(',')
                if len(data) == 3:
                    kode_buku = data[0].strip()
                    judul = data[1].strip()
                    harga = data[2].strip()
                    
                    # Menyimpan ke dalam dictionary dengan kode_buku sebagai key
                    database_buku[kode_buku] = {'judul': judul, 'harga': harga}
    else:
        print(f"Peringatan: File '{nama_file}' tidak ditemukan. Pastikan file sudah dibuat.")
        
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI
class Node:
    def __init__(self, judul):
        """Inisialisasi Node baru yang berisi judul buku dan pointer next"""
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
        """Inisialisasi Single Linked List kosong"""
        self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku baru ke akhir daftar promosi (Linked List)"""
        node_baru = Node(judul)
        
        # Jika linked list masih kosong, jadikan node baru sebagai head
        if not self.head:
            self.head = node_baru
            print(f"Buku '{judul}' berhasil ditambahkan ke daftar promosi.")
            return
            
        # Jika tidak kosong, telusuri sampai node terakhir
        current = self.head
        while current.next:
            current = current.next
            
        # Tambahkan node baru di akhir
        current.next = node_baru
        print(f"Buku '{judul}' berhasil ditambahkan ke daftar promosi.")

    def tampilkan_promosi(self):
        """Menampilkan semua judul buku dalam daftar promosi"""
        if not self.head:
            print("Daftar buku promosi saat ini kosong.")
            return
            
        print("\n--- Daftar Buku Promosi ---")
        current = self.head
        no = 1
        while current:
            print(f"{no}. {current.judul}")
            current = current.next
            no += 1

# 3. QUEUE - ANTREAN KASIR
class AntreanKasir:
    def __init__(self):
        """Inisialisasi struktur data antrean menggunakan List"""
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Menambah pelanggan ke dalam antrean (Enqueue - konsep FIFO)"""
        self.antrean.append(nama_pelanggan)
        print(f"Pelanggan '{nama_pelanggan}' telah masuk ke antrean.")

    def layani_pelanggan(self):
        """Melayani dan menghapus pelanggan dari antrean (Dequeue - konsep FIFO)"""
        if self.antrean:
            # Menghapus elemen pertama (index 0) sesuai prinsip First In First Out
            pelanggan_dilayani = self.antrean.pop(0)
            print(f"Pelanggan '{pelanggan_dilayani}' sedang dilayani.")
        else:
            print("Antrean saat ini kosong. Tidak ada pelanggan yang dilayani.")

# 4. SORTING - LAPORAN TRANSAKSI
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual dari terkecil ke terbesar
    menggunakan algoritma Insertion Sort.
    """
    # Algoritma Insertion Sort
    for i in range(1, len(list_harga)):
        key = list_harga[i]
        j = i - 1
        
        # Pindahkan elemen yang lebih besar dari key ke satu posisi di depannya
        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j]
            j -= 1
            
        # Tempatkan key pada posisi yang benar
        list_harga[j + 1] = key
        
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    
    # Data list transaksi sesuai spesifikasi soal
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku (Key: Kode, Value: Data):")
            if data_buku:
                for kode, info in data_buku.items():
                    print(f"Kode: {kode} | Judul: {info['judul']} | Harga: {info['harga']}")
            else:
                print("Katalog kosong. Pastikan file 'buku.txt' memiliki data yang benar.")
        
        elif pilihan == '2':
            print("\n--- Menu Promosi ---")
            print("a. Tambah Buku Promosi")
            print("b. Tampilkan Daftar Promosi")
            sub_pilihan = input("Pilih aksi (a/b): ").lower()
            
            if sub_pilihan == 'a':
                judul_baru = input("Masukkan judul buku untuk promosi: ")
                list_promosi.tambah_buku_promosi(judul_baru)
            elif sub_pilihan == 'b':
                list_promosi.tampilkan_promosi()
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '3':
            print("\n--- Menu Antrean ---")
            print("a. Tambah Antrean")
            print("b. Layani Pelanggan (Hapus Antrean)")
            sub_pilihan = input("Pilih aksi (a/b): ").lower()
            
            if sub_pilihan == 'a':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif sub_pilihan == 'b':
                antrean_toko.layani_pelanggan()
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '4':
            print("\nHarga Sebelum Urut:", riwayat_transaksi)
            # Menggunakan copy agar list asli tidak berubah permanen (opsional, tapi disarankan)
            list_kopian = riwayat_transaksi.copy()
            hasil_sort = urutkan_transaksi(list_kopian)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
            
        else:
            print("Pilihan tidak valid1! Silakan masukkan angka 1-5.")

if __name__ == "__main__":
    main()