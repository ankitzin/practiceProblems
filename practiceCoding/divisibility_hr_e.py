N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
num = ""
for val in data:
    num += str(val%10)

if int(num)%10 == 0:
    ans = 'Yes'
else:
    ans = 'No'


print(ans)