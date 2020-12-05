import math


def jump_search(arr, val):
    length = len(arr)
    jump = int(math.sqrt(length))
    left, right = 0, 0

    while left < length and arr[left] <= val:
        right = min(length - 1, left + jump)
        if arr[left] <= val <= arr[right]:
            break
        left += jump

    if left >= length or arr[left] > val:
        return -1

    right = min(length - 1, right)
    i = left
    while i <= right and arr[i] <= val:
        if arr[i] == val:
            return i
        i += 1
    return -1


print(jump_search([1, 2, 3, 4, 9, 19, 45], 19))
