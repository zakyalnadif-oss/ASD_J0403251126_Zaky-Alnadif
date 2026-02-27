# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Latihan 4: Kombinasi Huruf
# ==========================================================


def kombinasi(n, hasil=""):
 if len(hasil) == n:
   print(hasil)
   return
 kombinasi(n, hasil + "A")
 kombinasi(n, hasil + "B")
kombinasi(2)


#Bagaimana Kombinasi Terbentuk?
#Jika panjang hasil sudah sama dengan n, maka cetak.
#Jika belum, fungsi akan:
#Menambahkan huruf "A"
#Menambahkan huruf "B"
#Lalu memanggil dirinya sendiri lagi.
# Artinya, setiap posisi memiliki 2 pilihan huruf: A atau B.
