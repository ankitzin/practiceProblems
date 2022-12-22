inputs = [3, 1, 2, 10, 1]

for k in range(1,len(inputs),1):
    inputs[k] = inputs[k] + inputs[k-1]

print(inputs)
# o(n)
# o(1)