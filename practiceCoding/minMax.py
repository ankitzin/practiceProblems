n = 6
a = {3, 2, 1, 56, 10000, 167}


def getMinMax(a, n):
    a = list(a)
    a.sort()
    if n > 0:
        # print("min =" + str(a[0]) + ",max = " + str(a[-1]))
        print(f"min= {a[0]}, max={a[-1]}", end="")
    else:
        pass
getMinMax(a, n)