import time


def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    end_time = time.time()
    return arr, end_time - start_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end_time = time.time()
    return arr, end_time - start_time


def print_iteration_results(iterations):
    print("First 5 iterations: ", iterations[:5])
    print("Last 5 iterations: ", iterations[-5:])


def print_execution_time(execution_time):
    print("Execution Time: %.6f seconds" % execution_time)


def print_before_after(before, after):
    print("Before Sorting: ", before)
    print("After Sorting: ", after)


def analyze_algorithm():
    print("Analysis Algorithm:")
    print("1. Worst Case: O(n^2)")
    print("   - Terjadi ketika elemen-elemen dalam list terurut secara terbalik.")
    print("2. Best Case: O(n)")
    print("   - Terjadi ketika elemen-elemen dalam list sudah terurut secara terbalik.")
    print("3. Average Case: O(n^2)")
    print("   - Pada kasus rata-rata, kompleksitas waktu Bubble Sort dan Insertion Sort adalah O(n^2).")


def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    print("Welcome to Sorting Program!")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Analysis Algorithm")
    choice = input("Enter your choice (1-3): ")
    print()

    if choice == '1':
        sorted_arr, execution_time = bubble_sort(arr.copy())
        print_before_after(arr, sorted_arr)
        print_iteration_results(sorted_arr)
        print_execution_time(execution_time)
    elif choice == '2':
        sorted_arr, execution_time = insertion_sort(arr.copy())
        print_before_after(arr, sorted_arr)
        print_iteration_results(sorted_arr)
        print_execution_time(execution_time)
    elif choice == '3':
        analyze_algorithm()
    else:
        print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()