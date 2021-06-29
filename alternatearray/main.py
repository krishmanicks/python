arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 9
max = arr[n - 1]
min = arr[0]
b = []
ptr = True
for i in range(n):

    if ptr == True:
        b.append(max)
        max = max - 1
        ptr = False
        print(b)
    else:
        b.append(min)
        min = min + 1
        ptr = True
        print(b)
print("\n", b)


