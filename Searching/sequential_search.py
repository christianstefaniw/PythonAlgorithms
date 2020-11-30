def sequential_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1


print(sequential_search([5,5,3,7,8,1], 5))