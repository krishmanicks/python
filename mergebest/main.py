def merge(a,b,m,n):
    for i in range(n-1,-1,-1):
        last = a[m-1]
        j=m-2

        while(j>=0 and a[j]> b[i]):
            a[j+1] = a[j]
            j-=1
            print(a, end=" ")
            print(b)

        if(j!=m-2 or last > b[i]):
            a[j+1] = b[i]
            b[i] = last
            print(a, end=" ")
            print(b)

    print(a, end=" ")
    print(b)

a = [1, 3, 5, 7]
b = [0, 2, 6, 8, 9]
m = len(a)
n = len(b)
merge(a, b, m, n)


