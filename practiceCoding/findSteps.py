# n = int(input())
# a = list(map(int,input().split(' ')))
# b = list(map(int,input().split(' ')))
# print("n = ",n)
# print("a = ",a)
# print("b = ",b)
# min_a = min(a)
# print("min_a = ", min_a)
# Iter = 0
# i=0
# while (i<n):
#     print("n = ", n)
#     print("i = ",i)
#     if(a[i]<b[i]):
#         Iter = -1
#         print("1st if = ",Iter)
#         break;
#     while((a[i]>min_a)):
#         print("i ,a[",i,"], b[",i,"]",a[i],b[i])
#         a[i] = a[i]-b[i]
#         Iter+=1
#         print("Changed a[i] ",a[i])
#         print("Else Iter ", Iter)
#     if(a[i]<b[i]):
#         Iter = -1
#         print("2nd If ",Iter)
#         break;
#     if(a[i]<min_a):
#         min_a = a[i]
#         i=0
#         print("min Change", min_a)
#     elif(min_a<0):
#         Iter = -1
#         break
#     else:
#         i+=1
# print(Iter)


n = int(input())

a =[int(x) for x in input().split()]

b =[int(x) for x in input().split()]

def compute(a, b, n):
    a_min = min(a)
    count = 0
    i = 0
    while i < n:
        while a[i] > a_min:
            a[i] = a[i] - b[i]
            count = count+1
            if a[i] == a_min:
                i=i+1
                if i == n:
                    break
                continue
            if a[i] < b[i]:
                count = -1
                break
            if a[i] < a_min:
                a_min = a[i]
                i = 0
                continue
        i = i+1
    print(count)

compute(a,b,n)