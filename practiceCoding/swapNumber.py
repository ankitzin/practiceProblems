number = int(input())  # Reading input from STDIN

for val in range(number):
    list_n = int(input())
    arr = []
    # for i in range(list_n):
    v = input()
    v_list = v.split(' ')

    arr = [int(i) for i in v_list]
    arr.sort()
    # swapping technique
    # temp = arr[-1]
    # arr[-1] = arr[-2]
    # arr[-2] = temp
    arr = [str(i) for i in arr]
    arr = " ".join(arr)
    print(arr)


