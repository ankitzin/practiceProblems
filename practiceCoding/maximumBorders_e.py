num = int(input())
arr2d = []
for val in range(0, num, 1):
    row = int(input())
    column = int(input())
    rows, cols = row, column
    for i in range(0, rows, 1):
        col = []
        for j in range(cols):
            col.append(input())
        arr2d.append(col)

    for i in range(rows):
        for j in range(cols):
            if arr2d[i][j] == '#' and arr2d[i][j+1] == "#":
                count = count+1
