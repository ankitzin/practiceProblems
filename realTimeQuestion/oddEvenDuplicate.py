arr = [1, 2, 9, 3, 4, 5, 6, 7, 8]


def duplication(arr):
    arr.sort()
    for i in range(0, len(arr) - 1, 1):
        if arr[i] == arr[i + 1]:
            return False
    return True


def check_val(arr):
    even_list = []
    odd_list = []
    if arr[0] % 2 == 0:
        even_list = [arr[i] % 2 for i in range(0, len(arr), 2)]
        odd_list = [arr[i] % 2 for i in range(1, len(arr), 2)]

    if arr[0] % 2 == 1:
        even_list = [arr[i] % 2 for i in range(1, len(arr), 2)]
        odd_list = [arr[i] % 2 for i in range(0, len(arr), 2)]

    if 1 in even_list and 0 in odd_list:
        res = False
    else:
        res = True
    if res:
        res = duplication(arr)
    return res


print(check_val(arr))