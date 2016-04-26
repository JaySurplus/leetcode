class Heap(object):

    def max_heapify(self, A, i):
        """
        :type A: list
        :type i: index at list
        :rtype : None
        """

        try:
            l = 2 * i + 1
            r = 2 * i + 2
            print l, r

            if l < len(A) and A[l] > A[i]:
                m = l
            else:
                m = i
            if r < len(A) and A[r] > A[m]:
                m = r
            if m != i:
                A[i], A[m] = A[m], A[i]
                print A
                self.max_heapify(A, m)

        except IndexError:
            print "Index %d out of range" % i

    def build_heap(self, A):
        """
        :type A: list
        :rtype :
        """
        for i in range((len(A) - 1) / 2, -1, -1):
            print i
            self.max_heapify(A, i)


a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Heap = Heap()

Heap.build_heap(b)
print b
