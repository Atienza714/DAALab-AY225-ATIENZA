import time

import os



def bubble_sort_descending(arr):

    start_time = time.time()

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] < arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:

            break

    end_time = time.time()

    return arr, end_time - start_time



if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))

    subfolder = 'PRELIM_LAB WORK 1-ATIENZA' 

    file_path = os.path.join(script_dir, subfolder, 'dataset.txt')

    if not os.path.exists(file_path):

        file_path = os.path.join(script_dir, 'dataset.txt')


    try:

        print(f"Attempting to load data from: {file_path}")

        with open(file_path, 'r') as file:

            data = [int(line.strip()) for line in file if line.strip()]

        
        print(f"Successfully loaded {len(data)} items. Sorting...")


        sorted_list, time_spent = bubble_sort_descending(data)

        
        for value in sorted_list:

            print(value)

        print("\n" + "="*30)

        print("Bubble Sort Descending Result")

        print(f"TOTAL ITEMS: {len(sorted_list)}")

        print(f"TIME SPENT: {time_spent:.6f} seconds")

        print("="*30)
    

    except FileNotFoundError:

        print("\n[ERROR]: dataset.txt not found!")

        print(f"I checked the subfolder '{subfolder}' and the main folder.")

        print("Please verify the file is named 'dataset.txt' and is in one of those spots.")