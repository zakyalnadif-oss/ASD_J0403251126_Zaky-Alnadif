def quicksort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    kiri = []
    kanan = []
    
    for x in data[1:]:
        if x <= pivot:
            kiri.append(x)
        else:
            kanan.append(x)
    return quicksort(kiri) + [pivot] + quicksort(kanan)

data = [8, 4, 3, 7, 10, 9, 8, 2,]

print ("data awal",data)

hasil = quicksort(data)

print ("data akhir", hasil)