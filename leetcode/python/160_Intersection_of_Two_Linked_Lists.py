"""
    160. Intersection of Two Linked Lists

    Write a program to find the node at which the intersection of two singly linked lists begins.


    For example, the following two linked lists:

    A:          a1 - a2
                        \
                         c1 - c2 - c3
                        /
    B:     b1 - b2 - b3
    begin to intersect at node c1.


    Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h1 = headA
        h2 = headB
        while h1 and h2:
            h1 = h1.next
            h2 = h2.next

        count = 0
        if h1:
            while h1:
                h1 = h1.next
                count += 1
            while count > 0:
                headA = headA.next
                count -= 1

        if h2:
            while h2:
                h2 = h2.next
                count += 1
            while count > 0:
                headB = headB.next
                count -= 1

        while headA != headB:

            headA = headA.next
            headB = headB.next

        return headA

    def getIntersectionNodeII(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa

a1 = ListNode('a1')
a2 = ListNode('a2')

b1 = ListNode('b1')
b2 = ListNode('b2')
b3 = ListNode('b3')

c1 = ListNode('c1')
c2 = ListNode('c2')
c3 = ListNode('c3')

a1.next = a2
a2.next = c1

b1.next = b2
b2.next = b3
b3.next = c1

c1.next = c2
c2.next = c3

sol = Solution()
print sol.getIntersectionNodeII(a1, b1).val
