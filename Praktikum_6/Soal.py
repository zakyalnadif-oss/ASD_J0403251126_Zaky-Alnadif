# Data skor tes potensi akademik
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Menyimpan data asli untuk mengetahui nomor kandidat
data_asli = data.copy()

# Fungsi Quick Sort Descending
def quickSortDescending(data):
    quickSortHelper(data, 0, len(data)-1)

def quickSortHelper(data, first, last):
    if first < last:
        split = partition(data, first, last)

        quickSortHelper(data, first, split-1)
        quickSortHelper(data, split+1, last)

def partition(data, first, last):
    pivot = data[first]
    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and data[left] >= pivot:
            left += 1

        while right >= left and data[right] <= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            data[left], data[right] = data[right], data[left]

    data[first], data[right] = data[right], data[first]

    return right


# Mengurutkan data
quickSortDescending(data)

print("Skor dari tertinggi ke terendah:")
print(data)

# Mengambil 5 skor tertinggi
top5 = data[:5]

print("\n5 skor tertinggi:")
print(top5)

# Menentukan kandidat yang lolos
print("\nKandidat yang lolos:")
for i in range(len(data_asli)):
    if data_asli[i] in top5:
        print("Kandidat", i+1, "dengan skor", data_asli[i])
