#Bubble Sort
mylist = [21,7,10,3,32,13,8,17]

for i in range(len(mylist)-1):
    swapped = False
    for j in range(len(mylist)-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swapped = True
    if not swapped:
        break

print(mylist)