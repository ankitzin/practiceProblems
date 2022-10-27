def mini_array(arr):
    i = 0
    mini = arr[0]
    index = 0
    while i < len(arr):
        if mini >= arr[i]:
            mini = arr[i]
            index = i
        i += 1

    return index

