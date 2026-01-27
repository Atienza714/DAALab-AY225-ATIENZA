import time
import os

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if not swapped: break
        return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]; j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]; j-= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]); right = merge_sort(arr[mid:])
    result = []; i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    subfolder = 'PRELIM_LAB WORK 2-ATIENZA'
    file_path = os.path.join(script_dir, subfolder, 'dataset.txt')
    if not os.path.exists(file_path):
        file_path = os.path.join(script_dir, 'dataset.txt')

    try:
        with open(file_path, 'r') as file:
            original_data = [int(line.strip()) for line in file if line.strip()]

        while True:
            print("\n" + "="*30)
            print("   SELECT SORTING METHOD")
            print("="*30)
            print("1. Bubble Sort (Slow)")
            print("2. Insertion Sort (Medium)")
            print("3. Merge Sort (Fast)")
            print("4. Exit Program")
            
            choice = input("\nEnter your choice (1-4): ")

            if choice == '4':
                print("Goodbye!")
                break

            data_copy = original_data.copy()
            start_time = time.time()

            if choice == '1':
                name = "Bubble Sort"
                sorted_list = bubble_sort(data_copy)
            elif choice == '2':
                name = "Insertion Sort"
                sorted_list = insertion_sort(data_copy)
            elif choice == '3':
                name = "Merge Sort"
                sorted_list = merge_sort(data_copy)
            else:
                print("Invalid choice! Please try again.")
                continue

            end_time = time.time()
            
           
            print(f"\n--- {name} Results ---")
            print(f"First 10 numbers: {sorted_list[:10]}")
            print(f"Time Taken: {end_time - start_time:.6f} seconds")

    except FileNotFoundError:
        print(f"Error: dataset.txt not found at {file_path}")