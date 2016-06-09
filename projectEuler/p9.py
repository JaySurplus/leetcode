def specialPythagoreanTriplet(n):
    for c in range(n/3+1,n/2):
        for a in range(1,(n-c)/2+1):
            if (a+c)*(n-a) == n*n/2:
                b = n - a - c
                return a,b,c
    return -1,-1,-1

res = specialPythagoreanTriplet(1000)
print res
print reduce(lambda x,y : x*y, res)
print sum(res)

