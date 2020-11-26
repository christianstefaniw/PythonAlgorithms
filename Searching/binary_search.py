def binary_search(arr, x):
    start = 0
    end = len(arr)-1

    while end >= start:
        mid = (end+start) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            end = mid - 1

        elif arr[mid] < x:
            start = mid + 1


    return -1

print(binary_search([1,7,9,87,102,204,500,600,700], 102))