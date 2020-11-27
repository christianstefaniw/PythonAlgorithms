def selection_sort(arr):

    for k in range(len(arr)):
        currLow = arr[k]
        currLowIndex = k


        for i in range(k+1, len(arr)):
            if arr[i] > currLow:
                currLow = arr[i]
                currLowIndex = i

        temp = arr[k]
        arr[k] = currLow
        arr[currLowIndex] = temp

    return arr

print(selection_sort([4,3,9,6,10]))