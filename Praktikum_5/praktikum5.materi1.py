# ==========================================================
# Nama :Zaky Alnadif
# NIM  : J0403251126
# Contoh Rekursi 1: Faktorial
# ==========================================================


def faktorial(n):
    # Fungsi untuk menghitung nilai faktorial dari n
    
    # Base case: jika n == 0, maka kembalikan 1
    # Karena secara matematis 0! = 1
    if n == 0:
        return 1
    
    # Recursive case: jika n > 0
    # Faktorial dihitung dengan mengalikan n dengan faktorial(n-1)
    # Artinya: n! = n × (n-1)!
    return n * faktorial(n - 1)

# Memanggil fungsi faktorial dengan nilai 5
# Hasilnya akan menghitung 5! = 5 × 4 × 3 × 2 × 1
print(faktorial(5))  # Output yang diharapkan: 120