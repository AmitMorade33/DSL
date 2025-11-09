class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"{data} inserted at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"{data} inserted as the first node.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"{data} inserted at the end.")

    def delete_node(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            print(f"{key} deleted from the list.")
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"{key} not found in the list.")
            return

        prev.next = temp.next
        print(f"{key} deleted from the list.")

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def main():
    ll = LinkedList()

    while True:
        print("\n=== Linked List Menu ===")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete a Node")
        print("4. Display List")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = input("Enter data to insert at beginning: ")
            ll.insert_at_beginning(data)
        elif choice == '2':
            data = input("Enter data to insert at end: ")
            ll.insert_at_end(data)
        elif choice == '3':
            key = input("Enter data to delete: ")
            ll.delete_node(key)
        elif choice == '4':
            ll.display()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()