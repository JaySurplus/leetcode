"""
	133. Clone Graph



"""

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        stack = [node]
        dic = {}
        dic[node] = root
        while stack:
            curr = stack.pop()
            for n in curr.neighbors:
                if n not in dic:
                    stack.append(n)
                    dic[n] = UndirectedGraphNode(n.label)
                dic[curr].neighbors.append(dic[n])
        return root
