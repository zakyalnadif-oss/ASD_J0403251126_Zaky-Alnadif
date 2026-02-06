#membaca seluruh isi file data
#===========================================================
# Praktikum 1 : Konsep ADT dan File Handling

print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    isi_file = file.read()
    print(isi_file)
    print("Tipe data isi_file:", type(isi_file))
print("===========================================================")

print("====membuka file baris per baris====")
with open("data_mahasiswa.txt", "r", encoding="utf-8")as file:
    jumlah_baris = 0
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("baris ke -",jumlah_baris,)
        print("isinya:", baris)    
print("===========================================================")

with open("data_mahasiswa.txt", "r", encoding = "utf-8")as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, umur= baris.split(",")
        print(f"NIM: {nim}, Nama: {nama}, Umur: {umur} tahun")
       
data_list = [] # inisialisai list untuk menampung data

with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip() # menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        data_list.append([nim,nama,int(nilai)])
print("====Menampilkan list====")
print(data_list)
print("Contoh record pertama", data_list[0])
print("Contoh record kedua", data_list[1])
print("Contoh record ketiga", data_list[2])
print("Contoh record keempat", data_list[3])
print("Contoh record kelima", data_list[4])
print("Contoh record keenam", data_list[5])
print("Contoh record ketujuh", data_list[6])
print("Contoh record kedelapan", data_list[7])
print("Contoh record kesembilan", data_list[8])
print("Contoh record kesepuluh", data_list[9])
print("Jumlah record pada list", len(data_list))