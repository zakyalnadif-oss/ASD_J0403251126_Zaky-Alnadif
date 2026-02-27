# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
 # Base case
  if index == len(data) - 1:
   return data[index]
 # Recursive case
  maks_sisa = cari_maks(data, index + 1)
  if data[index] > maks_sisa:
   return data[index]
  else:
   return maks_sisa
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# 1. base case
# Base case terjadi saat index berada pada elemen terakhir list
# - jika index sudah mencapai elemen terakhir
# - Maka langsung kembalikan nilai tersebut,
# - Karena tidak ada lagi elemen untuk dibandingkan. 

# 2. recursive case
# maks_sisa = cari_maks(data, index + 1)
# - Fungsi memanggil dirinya sendiri dengan index yang lebih besar
# - Ini akan terus terjadi hingga mencapai base case
# - Setelah mencapai base case, fungsi mulai kembali (naik rekursi)
# - Pada setiap langkah naik, fungsi membandingkan nilai saat ini dengan hasil dari pemanggilan rekursif
# - Jika nilai saat ini lebih besar, kembalikan nilai saat ini
# - Jika tidak, kembalikan hasil dari pemanggilan rekursif (maks_sisa)

# 3. alur eksekusi
# cari_maks([3, 7, 2, 9, 5], index=0)
# = max(3, cari_maks([3, 7, 2, 9, 5], index=1))
# = max(3, max(7, cari_maks([3, 7, 2, 9, 5], index=2)))
# = max(3, max(7, max(2, cari_maks([3, 7, 2, 9, 5], index=3))))
# = max(3, max(7, max(2, max(9, cari_maks([3, 7, 2, 9, 5], index=4)))))
# = max(3, max(7, max(2, max(9, 5))))
# = max(3, max(7, max(2, 9)))
# = max(3, max(7, 9))
# = max(3, 9)
# = 9
