#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

# Version 1: BFS
# TC: O(n), SC: O(n)
class Solution:
    
    def findCousinSum(self,root, key):
        # code here
        res = {}
        current = set([(root, None)])
        while current:
            nextStep = set()
            cousin = {}
            total = 0
            for node, p in current:
                if p not in cousin:
                    cousin[p] = 0
                cousin[p] += node.data
                total += node.data
                if node.left:
                    nextStep.add((node.left, node))
                if node.right:
                    nextStep.add((node.right, node))
            for node, p in current:
                if len(cousin) > 1:
                    res[node.data] = total - cousin[p]
                else:
                    res[node.data] = -1
            current = nextStep
        return res[key]