def selection_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries


def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n):
        for j in range(0, n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries


def main():
    n = int(input("Enter the number of employees: "))
    salaries = []

    for i in range(n):
        sal = float(input(f"Enter salary for employee {i + 1}: "))
        salaries.append(sal)

    print("\nOriginal Salaries:", salaries)

    sel_sorted = selection_sort(salaries.copy())
    print("Salaries after Selection Sort:", sel_sorted)

    bub_sorted = bubble_sort(salaries.copy())
    print("Salaries after Bubble Sort:", bub_sorted)


if __name__ == "__main__":
    main()
