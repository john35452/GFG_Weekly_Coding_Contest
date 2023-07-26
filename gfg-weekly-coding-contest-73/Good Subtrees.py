#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    # Version 1: DFS
    # Return the frequency of each value
    # TC: O(n), SC: O(n)
    '''
    def goodSubtrees(self, root, k):
        #code here
        
        def dfs(node, ans):
            if node is None:
                return {}
            res = {node.data : 1}
            left = dfs(node.left, ans)
            right = dfs(node.right, ans)
            for key, v in left.items():
                if key not in res:
                    res[key] = 0
                res[key] += v
            for key, v in right.items():
                if key not in res:
                    res[key] = 0
                res[key] += v
            if len(res) <= k:
                ans[0] += 1
            return res
            
        ans = [0]
        dfs(root, ans)
        return ans[0]
    '''
    
    # Version 2: Use bitmask for the occurrence of each number
    # TC: O(n), SC: O(n)
    def goodSubtrees(self, root, k):
        #code here
        
        def dfs(node, ans):
            if node is None:
                return 0
            res = (1<<node.data)
            res = res | dfs(node.left, ans) | dfs(node.right, ans)
            if bin(res).count("1") <= k:
                ans[0] += 1
            return res
            
        ans = [0]
        dfs(root, ans)
        return ans[0]
