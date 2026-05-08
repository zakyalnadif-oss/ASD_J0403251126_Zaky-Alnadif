#=================================================================
# Nama : Zaky Alnadif
# NIM : J0403251126
# Deskripsi :Membuat Adjacency List
#=================================================================

# Praktikum 2 - Membuat Adjacency List

# Graph:
# A --- B
# |     |   
# C --- D

# Dictionary digunakan untuk menyimpan adjacency list
# key: vertex, value: list of adjacent vertices
# Value = list tangga (node yang terhubung)
graph = {
    'A': ['B', 'C'],  # Vertex A terhubung ke B dan C
    'B': ['A', 'D'],  # Vertex B terhubung ke A dan D
    'C': ['A', 'D'],  # Vertex C terhubung ke A dan D
    'D': ['B', 'C']   # Vertex D terhubung ke B dan C

}
# Menampilkan adjacency list
print("Adjacency List Representation:")
for node, tetagga in graph.items():
    print(node, ":", tetagga)

# Penjelasan:
# 1. A -> ['B', 'C'] menunjukkan bahwa vertex A terhubung ke vertex B dan C.
# 2. B -> ['A', 'D'] menunjukkan bahwa vertex B terhubung ke vertex A dan D.
# 3. C -> ['A', 'D'] menunjukkan bahwa vertex C terhubung ke vertex A dan D.
# 4. D -> ['B', 'C'] menunjukkan bahwa vertex D terhubung ke vertex B dan C.
