import time
import os
import csv


class Record:
    def __init__(self, id_val, first_name, last_name):
        self.id = int(id_val) 
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.id:<10} | {self.first_name:<15} | {self.last_name:<15}"


def get_val(record, column):
    if column == '1': return record.id
    if column == '2': return record.first_name.lower()
    return record.last_name.lower()



def bubble_sort(arr, col):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if get_val(arr[j], col) > get_val(arr[j+1], col):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr

def insertion_sort(arr, col):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and get_val(arr[j], col) > get_val(key, col):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr, col):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], col)
    right = merge_sort(arr[mid:], col)
    return merge(left, right, col)

def merge(left, right, col):
    res = []; i = j = 0
    while i < len(left) and j < len(right):
        if get_val(left[i], col) < get_val(right[j], col):
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def main():
   
    script_dir = os.path.dirname(os.path.abspath(__file__))
   
    file_path = os.path.join(script_dir, "..", "data", "generated_data.csv")
    
    print("--- PHASE 1: DATA PARSING ---")
    start_load = time.time()
    all_data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data.append(Record(row['ID'], row['FirstName'], row['LastName']))
        load_time = time.time() - start_load
        print(f"Loaded {len(all_data)} records from CSV.")
        print(f"File Load Time: {load_time:.4f}s\n")
    except FileNotFoundError:
        print(f"ERROR: CSV not found at {file_path}")
        print("Check if your CSV is in the 'data' folder and code is in 'src'.")
        return

    while True:
        print("="*25)
        print("      Sort Tool")
        print("="*25)
        
        try:
            # Scalability
            n = int(input(f"Enter N to sort (1 to {len(all_data)}): "))
            if n > len(all_data): n = len(all_data)
            
            # Column Selection 
            print("\nSelect Column: [1] ID  [2] FirstName  [3] LastName")
            col = input("Choice: ")
            
            # Algorithm Selection 
            print("\nAlgorithm: [1] Bubble  [2] Insertion  [3] Merge")
            algo = input("Choice: ")

            # Performance Warning 
            if algo in ['1', '2'] and n > 15000:
                print(f"\n[!] WARNING: O(n^2) algorithms are extremely slow for N={n}.")
                if input("Continue anyway? (y/n): ").lower() != 'y': continue

            data_to_sort = all_data[:n]
            print(f"\nSorting {n} records...")

            # Performance Tracking 
            start_sort = time.time()
            if algo == '1': sorted_list = bubble_sort(data_to_sort, col)
            elif algo == '2': sorted_list = insertion_sort(data_to_sort, col)
            else: sorted_list = merge_sort(data_to_sort, col)
            sort_time = time.time() - start_sort

            # Output Results (First 10)
            print("\n--- SORTED RESULTS (TOP 10) ---")
            print(f"{'ID':<10} | {'First Name':<15} | {'Last Name':<15}")
            print("-" * 45)
            for r in sorted_list[:10]: print(r)
            print("-" * 45)
            print(f"Sort Execution Time: {sort_time:.6f} seconds")

        except ValueError:
            print("Please enter a valid number for N.")
        
        if input("\nRun another test? (y/n): ").lower() != 'y': break

if __name__ == "__main__":
    main()