t = int(input())
for i in range(t):
    n, m = list(map(int,input().split()))
    b = []
    for j in range(n):
        r = input()
        b.append(r.count('#'))
    print(max(b))