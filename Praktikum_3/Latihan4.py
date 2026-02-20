class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Menampilkan isi linked list
    def display(self):
        if self.head is None:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Menggabungkan dua linked list
    def merge(self, other_list):
        merged_list = LinkedList()

        # Salin elemen dari list pertama
        temp = self.head
        while temp:
            merged_list.append(temp.data)
            temp = temp.next

        # Salin elemen dari list kedua
        temp = other_list.head
        while temp:
            merged_list.append(temp.data)
            temp = temp.next

        return merged_list


# ==========================
# Program Utama
# ==========================

list1 = LinkedList()
list2 = LinkedList()

# Input Linked List 1
input1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan koma): ")

if input1.strip() != "":
    elements1 = input1.split(",")
    for el in elements1:
        list1.append(int(el.strip()))

# Input Linked List 2
input2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan koma): ")

if input2.strip() != "":
    elements2 = input2.split(",")
    for el in elements2:
        list2.append(int(el.strip()))

# Tampilkan List 1
print("Linked List 1:", end=" ")
list1.display()

# Tampilkan List 2
print("Linked List 2:", end=" ")
list2.display()

# Gabungkan
merged = list1.merge(list2)

print("Linked List setelah digabungkan:", end=" ")
merged.display()
