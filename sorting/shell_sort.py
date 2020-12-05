def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            k = i

            while k >= gap and arr[k - gap] > temp:
                arr[k] = arr[k - gap]
                k -= gap

            arr[k] = temp

        gap //= 2

    return arr


print(shell_sort([4, 6, 8, 3, 2, 1, 6]))
