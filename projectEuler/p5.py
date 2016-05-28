"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""





def p5(n):
    _gcd = lambda x, y: x if y == 0 else _gcd(y, x % y) if x > y else _gcd(x, y % x)
    _lcm = lambda x, y: x * y / _gcd(x, y)
    res = reduce(_lcm, range(2, n + 1))
    return res

print p5(20)
