#=================================================================
# Nama : Zaky Alnadif
# NIM : J0403251126
# Deskripsi : Membuat graph menggunakan adjacency matrix
#=================================================================

def createGraph(V, edges):
    # Membuat matrix V x V berisi 0
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Menambahkan setiap edge ke adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]

        mat[u][v] = 1

        # Karena graph tidak berarah
        mat[v][u] = 1

    return mat


if __name__ == "__main__":
    # Jumlah vertex: 4 (0,1,2,3)
    V = 4

    # Daftar edge sesuai graph pada soal
    edges = [
        [0, 1],  # 0 - 1
        [0, 2],  # 0 - 2
        [1, 3],  # 1 - 3
        [2, 3]   # 2 - 3
    ]

    # Membuat graph
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

# Penjelasan:
# 1. V = 4 menunjukkan jumlah vertex dalam graph, yaitu 0, 1, 2, dan 3.
# 2. edges adalah daftar pasangan vertex yang terhubung oleh edge. Misalnya, [0, 1] berarti ada edge antara vertex 0 dan vertex 1.
# 3. Arti Baris Matrix:
#    - Baris 0: Vertex 0 terhubung ke vertex 1 dan 2 (nilai 1 di kolom 1 dan 2).
#    - Baris 1: Vertex 1 terhubung ke vertex 0 dan 3 (nilai 1 di kolom 0 dan 3).
#    - Baris 2: Vertex 2 terhubung ke vertex 0 dan 3 (nilai 1 di kolom 0 dan 3).
#    - Baris 3: Vertex 3 terhubung ke vertex 1 dan 2 (nilai 1 di kolom 1 dan 2).
