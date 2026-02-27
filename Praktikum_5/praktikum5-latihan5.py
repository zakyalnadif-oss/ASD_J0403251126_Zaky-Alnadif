# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Studi Kasus: Generator PIN
# ==========================================================


def buat_pin(panjang, hasil=""):
 if len(hasil) == panjang:
  print("PIN:", hasil)
  return
 for angka in ["0", "1", "2"]:
  buat_pin(panjang, hasil + angka)
buat_pin(3)

# Bagaimana cara mencegah angka yang sama muncul berulang?

#1Tambahkan kondisi if angka not in hasil
#def buat_pin(panjang, hasil=""):
    #if len(hasil) == panjang:
        #print("PIN:", hasil)
        #return
    #for angka in ["0", "1", "2"]:
        #if angka not in hasil:   # Cegah angka yang sudah dipakai
            #buat_pin(panjang, hasil + angka)

#buat_pin(3)
#2Dengan begitu, setiap digit hanya digunakan satu kali
#3Jumlah kombinasi berubah dari 3ⁿ (kombinasi dengan pengulangan) menjadi permutasi (tanpa pengulangan)