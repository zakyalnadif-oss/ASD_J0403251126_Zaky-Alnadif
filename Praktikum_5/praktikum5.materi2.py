# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================


def hitung(n):
    # Fungsi rekursif untuk menampilkan proses masuk (stacking)
    # dan keluar (unwinding) dalam rekursi
    
    # Base case: jika n == 0
    # Rekursi berhenti di sini
    if n == 0:
        print("Selesai")  # Ditampilkan saat sudah mencapai kondisi berhenti
        return            # Menghentikan pemanggilan fungsi
    
    # Ditampilkan sebelum pemanggilan rekursif
    # Ini disebut fase stacking (fungsi terus masuk ke dalam)
    print("Masuk:", n)
    
    # Pemanggilan rekursif dengan nilai n dikurangi 1
    # Masalah diperkecil hingga mencapai base case
    hitung(n - 1)
    
    # Ditampilkan setelah pemanggilan rekursif selesai
    # Ini disebut fase unwinding (fungsi kembali satu per satu)
    print("Keluar:", n)

# Memanggil fungsi dengan nilai awal 3
hitung(3)
