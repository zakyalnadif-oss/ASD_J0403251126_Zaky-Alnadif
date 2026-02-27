# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================


def biner(n, hasil=""):
    # Fungsi rekursif untuk menghasilkan semua kombinasi
    # bilangan biner sepanjang n digit
    
    # Base case:
    # Jika panjang string 'hasil' sudah sama dengan n,
    # artinya kombinasi sudah lengkap
    if len(hasil) == n:
        print(hasil)   # Cetak hasil kombinasi biner
        return         # Hentikan rekursi untuk cabang ini
    
    # Recursive case (Choose + Explore):
    
    # Pilihan 1: tambahkan karakter '0'
    # Lalu lanjutkan rekursi untuk mengisi digit berikutnya
    biner(n, hasil + "0")
    
    # Pilihan 2: tambahkan karakter '1'
    # Lalu lanjutkan rekursi untuk mengisi digit berikutnya
    biner(n, hasil + "1")

# Memanggil fungsi untuk menghasilkan
# semua kombinasi biner sepanjang 3 digit
biner(3)
