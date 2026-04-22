def qvick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return qvick_sort(less) + [pivot] + qvick_sort(greater)

