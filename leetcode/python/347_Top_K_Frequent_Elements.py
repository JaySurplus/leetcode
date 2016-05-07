"""
    347. Top K Frequent Elements
"""
import heapq

class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        l = [(key, v) for key, v in dic.iteritems()]

        heap = Heap()

        heap.build_heap(l[:k])

        for ele in l[k:]:
            heap.insert_top(ele)
        #print heap
        #returned_pairs = heap.return_heap()
        #returned_pairs.reverse()
        res = [ele[0] for ele in heap.get()]
        return res


    def topKFrequentII(self, nums, k):

        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        l = [(v, key) for key, v in dic.iteritems()]

        temp_heap = l[:k]
        print temp_heap
        for num in l[k:]:
            heapq.heappushpop(temp_heap, num)
            print temp_heap
        res = [v for k , v in temp_heap]

        return res

class Heap(object):

    def __init__(self, size=None):
        self.heap = []
        self.size = size


    def __repr__(self):
        return repr(self.heap)

    def get(self):
        return self.heap

    def build_heap(self, eles):
        self.heap = []
        for ele in eles:
            self.heap.append(ele)
            self.shift_up()

        return self.heap



    def shift_up(self):
        i = len(self.heap) - 1
        p = (i - 1) / 2

        while p >= 0 and self.heap[i][1] < self.heap[p][1]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            p = (i - 1) / 2
        # print self.heap

    def insert_top(self, ele):
        if ele[1] > self.heap[0][1]:
            self.heap[0] = ele
            self.shift_down()

    def compare(self, comp1, comp2):
        if comp1[1] > comp2[1]:
            return True
        else:
            return False

    def shift_down(self, heap=None):

        i = 0
        if heap:
            self.heap = heap
        while i * 2 + 1 < len(self.heap):

            if i * 2 + 2 >= len(self.heap):
                if self.compare(self.heap[i], self.heap[i * 2 + 1]):

                    self.heap[i], self.heap[
                        i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
                else:
                    break
            else:

                if self.compare(self.heap[i * 2 + 1], self.heap[i * 2 + 2]):
                    child = i * 2 + 2
                else:
                    child = i * 2 + 1

                if self.compare(self.heap[i], self.heap[child]):
                    self.heap[i], self.heap[
                        child] = self.heap[child], self.heap[i]
                    i = child
                else:
                    break

    def return_heap(self):
        heap_copied = self.heap
        res = []
        while heap_copied:
            res.append(heap_copied[0])
            heap_copied[0] = heap_copied[-1]
            heap_copied = heap_copied[:-1]
            self.shift_down(heap_copied)
        return res

sol = Solution()
res = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print res
res = sol.topKFrequentII([5,5,5,5,5,5,5,1, 1, 1, 1,1 , 2,2,2,2,3,3,3,4,4,5], 3)
print res
