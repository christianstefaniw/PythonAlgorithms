def bubble_sort(arr):
    for passNum in range(len(arr)-1, 0, -1):
        for i in range(passNum):
            if arr[i] > arr[i+1]:
                tmp =  arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
    return arr

print(bubble_sort([5,2,7,8,4,1]))

