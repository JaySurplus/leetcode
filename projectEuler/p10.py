"""
    problem 10
    The sum of the primes below 10 is 2+3+5+7=17

    Find the sum of all the primes below two million
"""
def sumOfPrimesBelow(n):
    res = 2
    table = [True for i in range(n)]
    for i in xrange(3,n,2):
        if table[i] == True:
            res += i
            for j in xrange(i**2,n,i):
                table[j] = False
    return res

res = sumOfPrimesBelow(200000)
print res


