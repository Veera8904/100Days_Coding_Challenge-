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

