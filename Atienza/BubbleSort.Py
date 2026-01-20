import time

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
    try:
        with open('dataset.txt', 'r') as file:
            data = [int(line.strip()) for line in file if line.strip()]
        
       
        sorted_list, time_spent = bubble_sort_descending(data)
        
      
        for value in sorted_list:
            print(value)
            
        
        print("\n" + "-"*30)
        print(f"Time spent: {time_spent:.6f} seconds")
        print("-"*30)

    except FileNotFoundError:
        print("Error: dataset.txt not found.")