import random
import time
import statistics
import matplotlib.pyplot as plt
import argparse

# ----- Define functions -----

def gen_rand_arr(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 1000000))
    return arr


def add_noise_to_sorted_arr(arr, noise_level):
    """
    Takes a sorted array and a noise level (0.05 for 5%, 0.2 for 20%),
    and performs a number of random swaps to create noise.
    """
    noisy_arr = arr.copy()
    n = len(noisy_arr)
    shuffle_count = int((n * noise_level) / 2)

    for i in range(shuffle_count):
        idx1 = random.randint(0, n - 1)
        idx2 = random.randint(0, n - 1)
        noisy_arr[idx1], noisy_arr[idx2] = noisy_arr[idx2], noisy_arr[idx1]

    return noisy_arr

def partition(A, p, r):
    x = A[r]  # pivot
    i = p - 1
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def selection_sort(A):
    n = len(A)
    
    # for j = 1 to n-1
    for j in range(n - 1):
        # Assume the first element is the minimum
        min_index = j
        
        # for i = j+1 to n
        for i in range(j + 1, n):
            
            # Find the smallest element in A[j...n-1]
            if A[i] < A[min_index]:
                min_index = i
        
        # Exchange A[j] with A[min_index]
        A[j], A[min_index] = A[min_index], A[j]
    
    return A


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i] # The current element to be positioned
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key at its correct position
        arr[j + 1] = key
        
    return arr


def merge_sort(A, p, r):
    
    """
        A (list): The array to be sorted.
        p (int): The starting index of the subarray.
        r (int): The ending index of the subarray.
    """

    if p >= r:
        return
        
    # middle point of array
    q = (p + r) // 2 
    
    merge_sort(A, p, q) # recursively sort A[p..q] 
    merge_sort(A, q + 1, r)  # recursively sort A[q + 1..r]
    
    # Merge A[p..q] and A[q + 1..r] into A[p..r]
    merge(A, p, q, r)


def merge(A, p, q, r):

    """
    merge two sorted subarrays:
    A[p..q] and A[q+1..r] into a single sorted subarray A[p..r].
    """
    # Calculate sizes of the two subarrays
    n1 = q - p + 1
    n2 = r - q
    
    # Create temporary arrays
    L = [0] * n1 
    R = [0] * n2
    
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
        
    # Merge the temp arrays back into main array
    i = 0  # Initial index of first subarray - L
    j = 0  # Initial index of second subarray - R
    k = p  # Initial index of merged subarray - A
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        
    # Copy any remaining elements of L[]
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
        
    # Copy any remaining elements of R[]
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def bubble_sort(A):

    n = len(A)
  
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                # Exchange A[j] with A[j - 1]
                A[j], A[j - 1] = A[j - 1], A[j]


#----Part D----

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--algorithms', type=int, nargs='+',choices=[1, 2, 3, 4, 5], required=True,
                    help='Algorithms to compare: 1-Bubble, 2-Selection, 3-Insertion, 4-Merge, 5-Quick')

parser.add_argument('-s', '--sizes', type=int, nargs='+', required=True,
                    help='Array sizes, 100 500 1000...')

parser.add_argument('-e', '--experiment', type=int, choices=[1, 2], required=True,
                    help='Experiment type: 1 - 5% noise, 2 - (20% noise)')

parser.add_argument('-r', '--repetitions', type=int, required=True,
                    help='Number of repetitions')

args = parser.parse_args()

array_size = args.sizes
repetitions = args.repetitions

if args.experiment == 1:
    noise_level = 0.05
else:
    noise_level = 0.20


algorithm_names = {
    1: 'Bubble Sort',
    2: 'Selection Sort',
    3: 'Insertion Sort',
    4: 'Merge Sort',
    5: 'Quick Sort'
}

algorithm_functions = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': lambda arr: merge_sort(arr, 0, len(arr) - 1),
    'Quick Sort': lambda arr: quicksort(arr, 0, len(arr) - 1)
}

selected_algs = [algorithm_names[alg_id] for alg_id in args.algorithms]


print("Running experiments with:")
print(f"Algorithms: {selected_algs}")
print(f"Sizes: {array_size}")
print(f"Noise: {int(noise_level * 100)}%")
print(f"Repetitions: {repetitions}\n")


# # ----Part B----

results_mean = {alg: [] for alg in selected_algs}
results_std = {alg: [] for alg in selected_algs}

Sorted_arrays = {f'size {size}': [] for size in array_size}

for size in array_size:
        print(f"Part B - size {size}")
        times = {alg: [] for alg in selected_algs}

        for rep in range(repetitions):
            arr = gen_rand_arr(size)


            for alg in selected_algs:
                arr_copy = arr.copy()
                start = time.time()
                algorithm_functions[alg](arr_copy)
                end = time.time()
                times[alg].append(end - start)

        for alg in selected_algs:
            results_mean[alg].append(statistics.mean(times[alg]))
            results_std[alg].append(statistics.stdev(times[alg]))


# array_size = [100, 500, 1000, 5000, 7500, 10000]
# repetitions = 5 # Number of times to repeat each experiment

# # Dictionaries to store the results (mean and standard deviation) for each algorithm
# results_mean = {'Insertion Sort': [], 'Merge Sort': [], 'Bubble Sort': []}
# results_std = {'Insertion Sort': [], 'Merge Sort': [], 'Bubble Sort': []}

# Sorted_arrays = {'size 100': [],'size 500': [], 'size 1000': [] 
#                 ,'size 5000': [],'size 7500': [], 'size 10000': [] }  #Dictionery that save the sorted arrays

# for size in array_size: 
    
#     print(f"Part B : Testing array size: {size}")
#     times = {'Insertion Sort': [], 'Merge Sort': [], 'Bubble Sort': []}

#     for rep in range(repetitions):
#         arr = gen_rand_arr(size)

#         # Insertion Sort
#         arr_copy = arr.copy()
#         start = time.time()
#         insertion_sort(arr_copy)
#         end = time.time()
#         times['Insertion Sort'].append(end - start)
#         Sorted_arrays[f'size {size}'].append(arr_copy.copy())

#         # Merge Sort
#         arr_copy = arr.copy()
#         start = time.time()
#         merge_sort(arr_copy, 0, len(arr_copy) - 1)
#         end = time.time()
#         times['Merge Sort'].append(end - start)

#         # Bubble Sort
#         arr_copy = arr.copy()
#         start = time.time()
#         bubble_sort(arr_copy)
#         end = time.time()
#         times['Bubble Sort'].append(end - start)

        
#     # Calculate mean and standard deviation for each algorithm at the current array size
#     for t in times:
#         mean_time = statistics.mean(times[t])
#         std_time = statistics.stdev(times[t]) 
        
#         results_mean[t].append(mean_time)
#         results_std[t].append(std_time)
        
print("Generating plot part B")

# # ---- Plotting the results ----
plt.figure()

for alg in selected_algs:
     means = results_mean[alg]
     stds = results_std[alg]
    
     # Plot the mean line
     plt.plot(array_size, means, marker='o', label=alg)
    
     # Plot a shaded region representing ±1 standard deviation around the mean runtime
     plt.fill_between(array_size, 
                [m - s for m, s in zip(means, stds)], 
                [m + s for m, s in zip(means, stds)], 
                alpha=0.2)
    
 # Set chart titles and labels
plt.title('Runtime Comparison (Random Arrays)')
plt.xlabel('Array size (n)')
plt.ylabel('Runtime (seconds)')
plt.legend()
plt.grid(True)

# Save the plot to a file 
plt.savefig('result1.png')
print("Plot saved as result1.png")


 # ----Part C----
 # save sorted version
Sorted_arrays[f'size {size}'].append(sorted(arr))

results_mean_c = {alg: [] for alg in selected_algs}
results_std_c = {alg: [] for alg in selected_algs}

for size in array_size:
    print(f"Part C - size {size}")
    times = {alg: [] for alg in selected_algs}

    for rep in range(repetitions):
        sorted_arr = Sorted_arrays[f'size {size}'][rep]
        noisy_arr = add_noise_to_sorted_arr(sorted_arr, noise_level)

        for alg in selected_algs:
            arr_copy = noisy_arr.copy()
            start = time.time()
            algorithm_functions[alg](arr_copy)
            end = time.time()
            times[alg].append(end - start)

    for alg in selected_algs:
        results_mean_c[alg].append(statistics.mean(times[alg]))
        results_std_c[alg].append(statistics.stdev(times[alg]))
# noise_level = 0.2

# # Dictionaries to store the results (mean and standard deviation) for each algorithm
# results_mean_c = {'Insertion Sort': [], 'Merge Sort': [], 'Bubble Sort': []} 
# results_std_c = {'Insertion Sort': [], 'Merge Sort': [], 'Bubble Sort': []}



# print(f"\n--- Starting Part C with {int(noise_level*100)}% noise ---")
    
# for size in array_size: 
        
#     print(f"Part C: Testing array size: {size}")
#     times = {'Insertion Sort': [], 'Merge Sort': [], 'Bubble Sort': []}

#     for rep in range(repetitions):
#         sorted_arr = Sorted_arrays[f'size {size}'][rep].copy()
#         noisy_arr = add_noise_to_sorted_arr(sorted_arr, noise_level)

#         # Insertion Sort
#         arr_copy = noisy_arr.copy()
#         start = time.time()
#         insertion_sort(arr_copy)
#         end = time.time()
#         times['Insertion Sort'].append(end - start)
            

#         # Merge Sort
#         arr_copy = noisy_arr.copy()
#         start = time.time()
#         merge_sort(arr_copy, 0, len(arr_copy) - 1)
#         end = time.time()
#         times['Merge Sort'].append(end - start)

#         # Bubble Sort
#         arr_copy = noisy_arr.copy()
#         start = time.time()
#         bubble_sort(arr_copy)
#         end = time.time()
#         times['Bubble Sort'].append(end - start)

            
#         # Calculate mean and standard deviation for each algorithm at the current array size
#     for t in times:
#         mean_time = statistics.mean(times[t])
#         std_time = statistics.stdev(times[t]) 
            
#         results_mean_c[t].append(mean_time)
#         results_std_c[t].append(std_time)
          
            
# print(f"Generating plot for {int(noise_level*100)}% noise")

    

# ---- Plotting the results ----
plt.figure()

for alg in results_mean:
    means = results_mean_c[alg]
    stds = results_std_c[alg]
        
# Plot the mean line
    plt.plot(array_size, means, marker='o', label=alg)
        
    # Plot a shaded region representing ±1 standard deviation around the mean runtime
    plt.fill_between(array_size, 
                [m - s for m, s in zip(means, stds)], 
                [m + s for m, s in zip(means, stds)], 
                alpha=0.2)
        
 # Set chart titles and labels
plt.title('Runtime Comparison (Nearly sorted arrays)')
plt.xlabel('Array size (n)')
plt.ylabel('Runtime (seconds)')
plt.legend()
plt.grid(True)

# Save the plot to a file 
plt.savefig('result2.png')
print("Plot saved as result2.png")


