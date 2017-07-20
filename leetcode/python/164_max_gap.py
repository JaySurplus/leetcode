#!
class Solution:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        # write your code here
        if len(nums) < 2:
            return 0
        max_num = -1
        min_num = 2 ** 31 - 1
        for n in nums:
            max_num = max(max_num, n)
            min_num = min(min_num, n)

        bu_size = int((max_num - min_num) / len(nums)) + 1
        bu_nums = int((max_num - min_num) / bu_size) + 1

        bu_list = [[2**31-1, -1] for i in range(bu_nums)]

        bu_eles = {}
        for n in nums:
            bu_index = int((n - min_num) / bu_size)
            bu_list[bu_index][0] = min(bu_list[bu_index][0], n)
            bu_list[bu_index][1] = max(bu_list[bu_index][1], n)
            bu_eles[bu_index] = 1

        pre = 0
        max_dist = 0
        for i in range(1, len(bu_list)):
            if i not in bu_eles:
                continue
            max_dist = max(max_dist, bu_list[i][0] - bu_list[pre][1])
            pre = i
        return max_dist

    def maximumGapII(self, num):
        N = len(num)
        if N < 2:
            return 0
        A = min(num)
        B = max(num)
        bucketRange = max(1, int((B - A - 1) / (N - 1)) + 1) #ceil( (B - A) / (N - 1) )
        bucketLen = (B - A) / bucketRange + 1
        buckets = [None] * bucketLen
        for K in num:
            loc = (K - A) / bucketRange
            bucket = buckets[loc]
            if bucket is None:
                bucket = {'min' : K, 'max' : K}
                buckets[loc] = bucket
            else:
                bucket['min'] = min(bucket['min'], K)
                bucket['max'] = max(bucket['max'], K)
        maxGap = 0
        for x in range(bucketLen):
            if buckets[x] is None:
                continue
            y = x + 1
            while y < bucketLen and buckets[y] is None:
                y += 1
            if y < bucketLen:
                maxGap = max(maxGap, buckets[y]['min'] - buckets[x]['max'])
            x = y
        return maxGap


if __name__ == '__main__':
    sol = Solution()
    case = [1,9,2,3,5]
    print(sol.maximumGap(case))
