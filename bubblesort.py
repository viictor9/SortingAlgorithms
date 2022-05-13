list = []
num = int(input("Enter the size of the list "))
for k in range(num):
    list.append(int(input("Enter the values of the list ")))

    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                print(list)
            else:
                print(list)
                print()

        print(list)
