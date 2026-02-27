# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================


def jumlah_list(data, index=0):
    # Fungsi rekursif untuk menghitung total/jumlah semua elemen dalam list
    
    # Base case:
    # Jika index sudah sama dengan panjang list,
    # artinya tidak ada elemen lagi yang bisa dijumlahkan
    if index == len(data):
        return 0  # Mengembalikan 0 sebagai nilai awal penjumlahan
    
    # Recursive case:
    # Mengambil elemen saat ini (data[index])
    # lalu menambahkan dengan hasil penjumlahan sisa elemen berikutnya
    return data[index] + jumlah_list(data, index + 1)

# Memanggil fungsi dengan list [2, 4, 6, 8]
# Prosesnya akan menjumlahkan 2 + 4 + 6 + 8
print(jumlah_list([2, 4, 6, 8]))  # Output yang diharapkan: 20