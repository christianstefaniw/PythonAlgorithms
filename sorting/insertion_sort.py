def insertion_sort(arr):
    for i in range(1, len(arr), 1):
        curr = arr[i]
        prevIndex = i - 1

        while prevIndex >= 0 and arr[prevIndex] > curr:
            arr[prevIndex+1] = arr[prevIndex]
            prevIndex -= 1

        arr[prevIndex+1] = curr

    return arr

print(insertion_sort([10,5,3,2,7,9,6,5,4]))