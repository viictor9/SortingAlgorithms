def selectionSort(list1):  #selection sort
    for i in range(len(list1)):
        min_val = min(list1[i:])
        j = list1.index(min_val)
        list1[i], list1[j] = list1[j], list1[i]


element = []
num = int(input("Enter the size of the list: "))
for k in range(num):
    element.append(int(input("Enter the elements for list ")))
    selectionSort(element)
    print(element)