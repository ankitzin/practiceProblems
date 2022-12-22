accounts = [[1,2,3],
            [3,2,1]]


def work(accounts):
    max_val = 0
    col = len(accounts)
    row = len(accounts[0])
    for i in range(col):
        for j in range(row):
            if max_val <= accounts[i][j]:
                max_val = accounts[i][j]
                result = (i,j)

    return accounts[result[0]][result[1]]

# print(work(accounts))


def work1(accounts):
    # O(n^2) and 0(1)
    max_val = 0
    col = len(accounts)
    row = len(accounts[0])
    for i in range(col):
        sum_row = 0
        for j in range(row):
            sum_row += accounts[i][j]

        if max_val <= sum_row:
            max_val = sum_row

    return max_val


print(work1(accounts))

def work2(accounts):
    # O(n^2) and 0(1)
    max_val = 0
    for i in range(len(accounts)):
        if max_val <= sum(accounts[i]):
            max_val = sum(accounts[i])
    return max_val

print(work2(accounts))