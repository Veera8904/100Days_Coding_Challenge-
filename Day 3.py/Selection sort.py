#Selection sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(len(mylist)):
    min_index = i
    for j in range(i+1, len(mylist)):
        if mylist[j] < mylist[min_index]:
            min_index = j
        mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print(mylist)
