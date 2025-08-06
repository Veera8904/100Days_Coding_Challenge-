
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


