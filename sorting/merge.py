# Implement a merge sort with recursion

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        print("Left Array - {} Right Array {}".format(leftarr, rightarr))

        # recursively break down the arrays
        mergeSort(leftarr)
        mergeSort(rightarr)
        print("Sorted Left Array - {} Sorted Right Array {}".format(leftarr, rightarr))

        # now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1
        print("Merged Array - {} ".format(dataset))

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

def main():
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Initial State : ", items)
    mergeSort(items)
    print("Final State : ", items)

if __name__ == "__main__":
    main()

# test the merge sort with data

