_arr = [1, 2, 3, 4]


def mult_all_values_in_list_indexing(arr):
    result = []
    left = 1
    for i in range(len(arr)):
        current_ = 1
        for ele in arr[i+1:]:
            current_ = ele * current_

        result.append(current_ * left)
        left = left * arr[i]
    return result


def mult_all_values_best(arr):
    left = 1
    product = []
    for ele in arr:
        product.append(left)
        left = left * ele

    right = 1
    for i in range(len(arr)-1, -1, -1):
        product[i] = product[i] * right
        right = right * arr[i]


print(mult_all_values_in_list_indexing(_arr))
print(mult_all_values_best(_arr))
