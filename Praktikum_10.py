# ===============================
# Praktikum 10 - Binary Tree Traversal
# Nama  : Zaky Alnadif
# NIM   : J0403251125
# ===============================

# Membuat class Node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Fungsi insert untuk Binary Search Tree
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data) 
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root

# Traversal In-order
def inorderTraversal(root, result):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.data)
        inorderTraversal(root.right, result)

# Traversal Pre-order
def preorderTraversal(root, result):
    if root:
        result.append(root.data)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)

# Traversal Post-order
def postorderTraversal(root, result):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        result.append(root.data)

# ===============================
# DATA BERDASARKAN NIM (26)
# ===============================
root_value = 26
data = [6, 46, 16, 36, 56, 11]

# Membuat tree
root = Node(root_value)

for d in data:
    insert(root, d)

# ===============================
# PROSES TRAVERSAL
# ===============================
inorder_result = []
preorder_result = []
postorder_result = []

inorderTraversal(root, inorder_result)
preorderTraversal(root, preorder_result)
postorderTraversal(root, postorder_result)

# ===============================
# OUTPUT
# ===============================
print("====================================")
print("Nama : Zaky Alnadif")
print("NIM  : J0403251125")
print("NIM Belakang : 26")
print("====================================\n")

print("Data yang dimasukkan:", [root_value] + data)

print("\nHasil Traversal:")
print("In-order  :", inorder_result)
print("Pre-order :", preorder_result)
print("Post-order:", postorder_result)