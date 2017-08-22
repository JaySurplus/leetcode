class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next


class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """

    def bstToDoublyList(self, root):
        # Write your code here
        if not root:
            return None
        head, end = self.helper(root)
        return head

    def helper(self, root):
        mid = DoublyListNode(root.val)
        head, end = mid, mid
        if root.left:
            head, end_l = self.helper(root.left)
            end_l.next = mid
            mid.prev = end_l
        if root.right:
            head_r, end = self.helper(root.right)
            mid.next = head_r
            head_r.prev = mid
        return (head, end)


if __name__ == '__main__':

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n4.left = n2
    n4.right = n5
    n2.left = n1
    n2.right = n3

    sol = Solution()
    res = sol.bstToDoublyList(n4)

    while res:
        print(res.val)
        if not res.next:
            break
        res = res.next
    print()
    while res:
        print(res.val)
        if not res.prev:
            break
        res = res.prev
