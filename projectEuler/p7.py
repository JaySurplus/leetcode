
def sieveOfEratosthenes(n):

    res = [True for i in range(n-1)]
    for i in range(int((n-2)**0.5)+1):
        if res[i] == True:
            j = (i+2)**2
            while j-2 < n-1:
                res[j-2] = False
                j += i+2

    res = [(i+2,res[i]) for i in range(len(res))]
    res = filter(lambda x: x[1] == True, res)
    print len(res)
    return res[10000]

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 and n>2:
        return True
    for i in range(3,int(n**0.5),2):
        if n%i == 0:
            return True
    return False


print sieveOfEratosthenes(10000000)
