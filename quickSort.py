def quickSort(sequence):  #quick sort
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

        items_greater = []
        items_lower = []

        for i in sequence:
            if i > pivot:
                items_greater.append(i)

            else:
                items_lower.append(i)

        return quickSort(items_lower) + [pivot] + quickSort(items_greater)


print(quickSort([25, 84, 12, 10, 47, 54, 63]))