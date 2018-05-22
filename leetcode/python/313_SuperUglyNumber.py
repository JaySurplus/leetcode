#!python

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]

        pointers = [0] * len(primes)
        while len(uglies) < n:
            min_Pos = uglies[-1]
            minNum = 2 ** 32
            for i in range(len(primes)):
                if primes[i] * uglies[pointers[i]] < minNum:
                    minNum = primes[i] * uglies[pointers[i]]
                    min_Pos = i
                elif primes[i] * uglies[pointers[i]] == minNum:
                    pointers[i] += 1
            uglies.append(minNum)
            pointers[min_Pos] += 1
        return uglies[-1]
            


        
if __name__ == "__main__":
    n = 12
    primes = [2, 7, 13, 19]
    sol = Solution()
    res = sol.nthSuperUglyNumber(n, primes)
    print(res)