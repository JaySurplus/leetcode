
def p6(n):
    res = 0
    total = sum(range(1, n + 1))
    for i in xrange(1, n):
        total -= i
        res += 2 * i * total
    return res


def p6_2(n):
    squareSum = lambda n: (n * (n + 1) / 2)**2
    sumSquare = lambda n: n * (n + 1) * (n * 2 + 1) / 6
    return squareSum(n) - sumSquare(n)

print p6_2(13211)
