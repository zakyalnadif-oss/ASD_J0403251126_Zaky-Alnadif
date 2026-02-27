# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
 if n == 0:
  print("Selesai")
  return
 print("Masuk:", n)
 countdown(n - 1)
 print("Keluar:", n)
countdown(3)


#Karena rekursi menggunakan Call Stack (tumpukan) yang bekerja dengan prinsip:
#LIFO (Last In, First Out)
#Yang terakhir masuk, keluar duluan.
#Urutannya seperti menumpuk piring:
#Masuk 3
#Masuk 2
#Masuk 1
#Selesai
#Keluar 1 (karena paling atas)
#Keluar 2
#Keluar 3

#Jadi:
#"Masuk" terjadi saat fungsi dipanggil (fase turun)
#"Keluar" terjadi saat fungsi selesai (fase naik)
#Karena fase naik berjalan dari dalam ke luar, maka hasilnya terlihat terbalik.