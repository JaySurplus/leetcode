"""
	138. Copy List with Random Pointer

	A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

	Return a deep copy of the list.		
"""


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution():
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype RandomListNode
		"""
		if not head:
			return None

		curr = head
		while curr:
			n = RandomListNode(curr.label)
			n.next = curr.next
			n.random = curr.random
			curr.next = n
			curr = n.next

		curr = head
		while curr:
			if curr.random:
				curr.next.random = curr.random.next
			curr = curr.next.next

	
		
		newHead = head.next
		curr = head
		curr2 = newHead
		while curr:
			curr.next = curr2.next
			if curr.next :
				curr2.next = curr.next.next
			else:
				curr2.next = None
			curr = curr.next
			curr2 = curr2.next
		return newHead
			
			

			



