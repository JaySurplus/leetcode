# Complete the extraLongFactorials function below.
import time


def summation(a, b, offset):
    """
    a, b are list of integers 
    b is shift by offset
    """
    res = []
    carry = 0
    res = a[:offset]
    for i in range(len(a)-offset):
        s = b[i] + a[i+offset] + carry
        res.append(s % 10)
        carry = 0 if s < 10 else 1
    for i in range(len(a)-offset, len(b)):
        s = b[i] + carry
        res.append(s % 10)
        carry = 0 if s < 10 else 1
    if carry:
        res.append(carry)
    return res


def multiplication(a, b):
    """
    input:
        a: integer in a reversed order list
        b: single digit
    return:
        result in a reversed order list
    """

    def _multi(a, s):
        """
        input: 
            a: integer in a reversed order list
            s: single digit
        return:
            result in a reversed order list
        """
        carry = 0
        temp_res = []
        for i in a:
            multi = i * s + carry
            temp_res.append(multi % 10)
            carry = multi // 10
        if carry:
            temp_res.append(carry)
        return temp_res
    res = []
    for offset in range(len(b)):
        res = summation(res, _multi(
            a, b[offset]), offset)
    return res


def extraLongFactorials(n):
    """Cheating"""
    res = [1]
    for i in range(1, n+1):
        reverse = list(map(int, list(str(i))[::-1]))
        res = multiplication(res, reverse)
    res = "".join(list(map(str, res[::-1])))
    return res


def dirty(n):
    res = 1
    i = 2
    while i <= n:
        res *= i
        i += 1
    return res


if __name__ == '__main__':
    n = 52
    res = ""
    a = 43210472147812741203476124
    b = 48912743287427423194923147
    t1 = time.time()
    la = list(map(int, str(a)[::-1]))
    lb = list(map(int, str(b)[::-1]))
    for i in range(10000):
        res = multiplication(
            la, lb)
    t2 = time.time()
    t3 = time.time()
    for i in range(10000):
        dirty_res = a * b
    t4 = time.time()
    print(res, t2 - t1)
    print(dirty_res, t4 - t3)
    print(res == dirty_res)
