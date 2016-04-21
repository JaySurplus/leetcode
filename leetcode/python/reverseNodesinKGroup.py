"""
	Reverse Nodes in K-Group


	Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

	If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

	You may not alter the values in the nodes, only nodes itself may be changed.

	Only constant memory is allowed.

	For example,
		Given this linked list: 1->2->3->4->5

		For k = 2, you should return: 2->1->4->3->5

		For k = 3, you should return: 3->2->1->4->5

	https://leetcode.com/problems/reverse-nodes-in-k-group/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tempHead = ListNode(0)
        tempHead.next = head
        curr = tempHead
        validCheck = curr
        isLast = False
        while True:
        	for i in range(k):
        		if validCheck.next :
        			validCheck = validCheck.next
        		else:
        			isLast = not isLast
        			break
        	if not isLast:
        		self.reverse(curr ,k)
        		self.moveByKnoReturn(curr, k-k/2)
        	if isLast:
        		break

        return tempHead.next
    def moveByKnoReturn(self, curr, k):
    	for i in range(k):
    		curr = curr.next
	def moveByK(self, curr, k):
		p = curr 
		for i in range(k):
			p = p.next
		return p

    def reverse(self , curr , k):
    	if k < 2:
    		return

    	if k == 2:
    		p = curr.next.next
    		curr.next.next = p.next
    		p.next = curr.next
    		curr.next = p
    		curr = p

    	else:
    		p1 = self.moveByK(curr, k)
    		p2 = self.moveByK(curr, 2)
    		p3 = self.moveByK(p2,k-3)
    	
    		p3.next = p1.next
    		curr.next.next = p3.next
    		p3.next = curr.next

    		p1.next = p2
    		curr.next = p1
    		curr = p1

    		self.reverse(curr , k -2)

