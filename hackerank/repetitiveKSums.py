"""
    Repetitive K-Sums
    https://www.hackerrank.com/challenges/repeat-k-sums/problem
"""
import sys
import time
sys.setrecursionlimit(2000)


def readfile(name):
    test_cases = []
    with open(name) as f:
        num = int(f.readline().strip())

        while num > 0:

            n, k = list(map(int, f.readline().strip().split(" ")))
            ksum = list(map(int, f.readline().strip().split(" ")))
            test_cases.append((n, k, ksum))
            num -= 1
    return test_cases


class Solution():

    def solver(self, n, k, ksum):
        self.res = []
        self.perm_dic = {}
        self.index_dic = {}
        self.removed = set()
        ksum.sort()

        for i in range(len(ksum)):
            if ksum[i] in self.index_dic:
                self.index_dic[ksum[i]].append(i)
            else:
                self.index_dic[ksum[i]] = [i]

        self.res = [ksum[-1] // k]
        i = len(ksum) - 1
        self.index_dic[ksum[i]].pop()
        if self.index_dic[ksum[i]] == []:
            del self.index_dic[ksum[i]]
        self.removed.add(i)

        index = i - 1
        self.helper(n, k, ksum, index)

        return self.res

    def helper(self, n, k, ksum, index):

        if index < 0:
            return
        if ksum == []:
            return

        self.res_temp = [ksum[index] - (self.res[-1] * (k-1))]
        self.res = self.res_temp + self.res

        if len(self.res) == n:
            return

        res_per = self.permutation(self.res, k)
        res_pre = self.permutation(self.res[1:], k)
        res_diff = res_per[:-len(res_pre)]
        res_per_sum = [sum(per) for per in res_diff]

        for s in res_per_sum:
            i = self.index_dic[s].pop()
            if len(self.index_dic[s]) == 0:
                del self.index_dic[s]
            self.removed.add(i)

        while index in self.removed:
            index -= 1

        self.helper(n, k, ksum, index)

    def permutation(self, l, n):
        if (tuple(l), n) in self.perm_dic:
            return self.perm_dic[(tuple(l), n)]
        if l == []:
            return []
        if n == 0:
            return [[]]
        self.perm_dic[(tuple(l), n)] = [
            [l[0]] + p for p in self.permutation(l, n - 1)] + self.permutation(l[1:], n)
        return self.perm_dic[(tuple(l), n)]


if __name__ == "__main__":
    sol = Solution()
    filepath = "./repetitiveKSums_tests.txt"

    test_cases = readfile(filepath)
    for cases in test_cases:
        n, k, ksum = cases
        t1 = time.time()
        res = sol.solver(n, k, ksum)
        t2 = time.time()
        print(t2 - t1)
        print(n, k, " ".join(list(map(str, res))))


