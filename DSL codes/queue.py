def enqueue(queue, item):
    queue.append(item)
    print(f"{item} added to the queue.")

def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty. Cannot dequeue.")
    else:
        removed = queue.pop(0)
        print(f"{removed} removed from the queue.")

def display(queue):
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Current Queue:", queue)

def main():
    queue = []

    while True:
        print("\n=== Queue Menu ===")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            enqueue(queue, item)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            display(queue)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()