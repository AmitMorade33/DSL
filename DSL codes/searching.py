def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    print("Search Menu:")
    print("1. Linear Search")
    print("2. Binary Search")
    choice = input("Enter your choice (1 or 2): ")

    arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
    target = int(input("Enter the number to search for: "))

    if choice == '1':
        result = linear_search(arr, target)
    elif choice == '2':
        arr.sort()  # Binary search needs sorted list
        print("Sorted list for binary search:", arr)
        result = binary_search(arr, target)
    else:
        print("Invalid choice.")
        return

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()