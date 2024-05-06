import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr[i:i + min_run])

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            merged_array = merge(arr[start:midpoint + 1], arr[midpoint + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array
        size *= 2

    return arr

# Генерація наборів даних різного розміру
sizes = [1000, 10000, 20000, 40000]
datasets = []
for size in sizes:
    dataset = [random.randint(1, 1000) for _ in range(size)]
    datasets.append(dataset)

# Тестування алгоритмів на різних наборах даних
for i, dataset in enumerate(datasets):
    print(f"Dataset size: {sizes[i]}")
    
    merge_sort_time = timeit.timeit(lambda: merge_sort(dataset.copy()), number=1)
    print(f"Merge Sort: {merge_sort_time:.5f} seconds")
    
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(dataset.copy()), number=1)
    print(f"Insertion Sort: {insertion_sort_time:.5f} seconds")
    
    timsort_time = timeit.timeit(lambda: timsort(dataset.copy()), number=1)
    print(f"Timsort: {timsort_time:.5f} seconds")
    
    print()