# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================


def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi rekursif untuk menghasilkan kombinasi biner sepanjang n digit
    # dengan batas maksimal jumlah angka '1' sebanyak 'batas'
    
    # Pruning (pemangkasan cabang):
    # Jika jumlah '1' sudah melebihi batas yang ditentukan,
    # maka hentikan rekursi pada cabang ini
    if jumlah_1 > batas:
        return
    
    # Base case:
    # Jika panjang string 'hasil' sudah sama dengan n,
    # artinya kombinasi sudah lengkap
    if len(hasil) == n:
        print(hasil)  # Cetak kombinasi yang memenuhi syarat
        return
    
    # Recursive case (Choose + Explore):
    
    # Pilihan 1: tambahkan '0'
    # jumlah_1 tidak berubah karena tidak menambah angka '1'
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Pilihan 2: tambahkan '1'
    # jumlah_1 bertambah 1 karena menambahkan angka '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Memanggil fungsi:
# Membuat kombinasi biner 4 digit
# dengan maksimal 2 angka '1'
biner_batas(4, 2)
