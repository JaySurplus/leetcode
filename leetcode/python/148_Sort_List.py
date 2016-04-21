"""
	148. Sort List

	Sort a linked list in O(n log n) time using constant space complexity.
"""
import os
import sys


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
        # Merge sort

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        def merge(head1, head2):

            dummy = ListNode(0)
            curr = dummy

            while head1 and head2:
                if head1.val <= head2.val:
                    curr.next = head1
                    head1 = head1.next

                else:
                    curr.next = head2
                    head2 = head2.next

                curr = curr.next

            if head1:
                curr.next = head1
            else:
                curr.next = head2

            return dummy.next

        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

        h1 = dummy.next
        h2 = slow.next
        slow.next = None

        left = self.sortList(h1)
        right = self.sortList(h2)

        return merge(left, right)

    # QuickSort
    def sortListII(self, head):
        if not head or not head.next:
            return head

        h1 = ListNode(None)
        c1 = h1

        h2 = ListNode(None)
        c2 = h2

        h3 = ListNode(None)
        c3 = h3

        curr = head
        p = head.val
        while curr:
            if curr.val < p:
                c1.next = curr
                c1 = c1.next
            elif curr.val == p:
                c2.next = curr
                c2 = c2.next
            else:
                c3.next = curr
                c3 = c3.next
            n = curr.next
            curr.next = None
            curr = n

        if not h1:
            c2.next = h3.next
            return c2

        sort_h1 = self.sortList(h1.next)
        sort_h3 = self.sortList(h3.next)

        if not sort_h1:
            c2.next = sort_h3
            return h2.next

        tail_1 = sort_h1
        while tail_1.next:
            tail_1 = tail_1.next

        tail_1.next = h2.next

        c2.next = sort_h3

        return sort_h1


def printList(head):
    if not head:
        return []

    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def createNodeList(aList):
    if not aList:
        return None
    dummy = ListNode('')
    curr = dummy
    for i in aList:
        ln = ListNode(i)
        curr.next = ln
        curr = curr.next
    return dummy.next


def main(argv):
    sol = Solution()

    aList = [3, 21, 32, 1, 2, 3, 5, 1, 23, 32, 1, 6, 4, 32]

    head = createNodeList(aList)

    res = printList(head)

    newHead = sol.sortListII(head)
    res = printList(newHead)
    print res

if __name__ == "__main__":
    main(sys.argv[1:])
