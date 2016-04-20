"""
	147. Insertion Sort List

	Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
import sys
import os


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        comp = dummy = ListNode('Dummy')
        dummy.next = head
        curr = head
        while curr.next:
            val = curr.next.val
            if val >= curr.val:
                curr = curr.next
            else:
                if comp.next.val >= val:
                    comp = dummy
                while comp.next.val < val:
                    comp = comp.next
                toIn = curr.next
                curr.next = toIn.next
                toIn.next = comp.next
                comp.next = toIn
        return dummy.next


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

    aList = [1,32,1,2,3,5,1,23,32,1,6,4,32]
    head = createNodeList(aList)

    res = printList(head)
    print res

    
    newHead = sol.insertionSortList(head)
    res = printList(newHead)
    print res

if __name__ == "__main__":
    main(sys.argv[1:])
