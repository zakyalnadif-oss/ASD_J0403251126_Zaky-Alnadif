class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)

        # Jika list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Fungsi pencarian
    def search(self, key):
        if self.head is None:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return

            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


# ==========================
# Program Utama (Main)
# ==========================

cll = CircularLinkedList()

# Input elemen
data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

if data_input.strip() == "":
    print("Masukkan elemen yang ingin dicari: ", end="")
    key = int(input())
    cll.search(key)
else:
    elements = data_input.split(",")

    for element in elements:
        cll.append(int(element.strip()))

    key = int(input("Masukkan elemen yang ingin dicari: "))
    cll.search(key)
