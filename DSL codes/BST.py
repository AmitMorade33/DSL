class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    elif value < root.data:
        return search(root.left, value)
    else:
        return search(root.right, value)

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete(root, value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# 🌟 Menu
def menu():
    root = None
    while True:
        print("\n--- BST Menu ---")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. In-order Traversal")
        print("5. Pre-order Traversal")
        print("6. Post-order Traversal")

        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            root = insert(root, val)
        elif choice == '2':
            val = int(input("Enter value to search: "))
            found = search(root, val)
            print("Found!" if found else "Not found.")
        elif choice == '3':
            val = int(input("Enter value to delete: "))
            root = delete(root, val)
        elif choice == '4':
            print("In-order Traversal:")
            inorder(root)
            print()
        elif choice == '5':
            print("Pre-order Traversal:")
            preorder(root)
            print()
        elif choice == '6':
            print("Post-order Traversal:")
            postorder(root)
            print()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()