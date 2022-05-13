def insertionSort(element): #insertion sort
    for i in range(1, len(element)):
        j = i
        while element[j-1] > element[j] and j > 0:
            element[j-1], element[j] = element[j], element[j-1]
            j -= 1


element = []
num = int(input("Enter the size of the element\t"))
for k in range(num):
    element.append(int(input("Enter the elements for the list to be sorted\t")))
    insertionSort(element)

    print(element)