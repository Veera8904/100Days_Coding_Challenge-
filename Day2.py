#Quick Sort
def partition(arr,low,high):
    pivot = arr[high] # choose the last elememnt as pivot
    i = low -1  # index of smaller element

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high] , arr[i+1]
    return i+1

def quicksort(arr,low = 0, high = None):
    if high == None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)


#Merge Sort
def mergesort(arr):
    #Base case: if the array is of length 0 or 1, it is already sorted
    if len(arr) <= 1:
        return arr
    
    #find the middle index and divide the array into two halves
    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    #recursively sort both halves
    sortedleft = mergesort(lefthalf)
    sortedright = mergesort(righthalf)
    
    return merge(sortedleft, sortedright)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
    
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergesort(mylist)
print("Sorted array:", mysortedlist)






