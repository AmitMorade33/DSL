def push(stack, item):
    stack.append(item)
    print(f"{item} pushed onto the stack.")

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty. Cannot pop.")
    else:
        removed = stack.pop()
        print(f"{removed} popped from the stack.")

def peek(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print(f"Top of the stack: {stack[-1]}")

def display(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Current Stack (top to bottom):")
        for item in reversed(stack):
            print(item)

def main():
    stack = []

    while True:
        print("\n=== Stack Menu ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to push: ")
            push(stack, item)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            peek(stack)
        elif choice == '4':
            display(stack)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()