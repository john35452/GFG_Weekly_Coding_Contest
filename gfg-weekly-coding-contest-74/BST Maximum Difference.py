#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    
    # Version 1: Find target number and get the minimum path sum from the target node
    # The difference in this problem is sum - path_sum rather than abs(sum - path_sum)
    # Therefore, we can just focus on minimum path sum.
    # TC: O(h) = O(n), SC: O(n)
    def maxDifferenceBST(self,root, target):
        #code here
        def dfs(node):
            if not node:
                return float('inf')
            res = min(dfs(node.left), dfs(node.right))
            if res == float('inf'):
                res = 0
            return res + node.data
        
        current = root
        total = 0
        while current:
            if current.data == target:
                break
            total += current.data
            if current.data > target:
                current = current.left
            else:
                current = current.right
        
        if not current:
            return -1
        return total - dfs(current) + current.data
