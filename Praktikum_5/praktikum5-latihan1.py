# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
 # Base case
 if n == 0:
   return 1
 # Recursive case
 return a * pangkat(a, n - 1)
print(pangkat(2, 4))


# tahap pemangilan fungsi:
# pangkat(2,4)
# = 2 * pangkat(2,3)
# = 2 * (2 * pangkat(2,2))
# = 2 * (2 * (2 * pangkat(2,1)))
# = 2 * (2 * (2 * (2 * pangkat(2,0))))
# Saat n == 0, fungsi mengembalikan 1.

# Tahap Pengembalian Nilai (Naik Rekursi)
# pangkat(2,0) = 1
# pangkat(2,1) = 2 * 1 = 2
# pangkat(2,2) = 2 * 2 = 4
# pangkat(2,3) = 2 * 4 = 8
# pangkat(2,4) = 2 * 8 = 16