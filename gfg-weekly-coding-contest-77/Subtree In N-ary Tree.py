#User function Template for python3

'''
class Node:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children or []
    
    def __str__(self):
        return str(self.key)
'''

class Solution:
    # Version 1: Pre-order traversal
    # Store all Pre-order string of every subtree
    # TC: O(n^2), SC: O(n^2)
    def duplicateSubtreeNaryTree(self, root):
        #code here

        def preOrder(node, count):
            if not node:
                return ""
            else:
                res = ["(" + str(node.key)]
                for child in node.children:
                    res.append("(" + preOrder(child, count) + ")")
                res.append(")")
                res = "".join(res)
                if res not in count:
                    count[res] = 0
                count[res] += 1
                return res
        
        count = {}
        preOrder(root, count)
        ans = 0
        for _, v in count.items():
            if v > 1:
                ans += 1
        return ans
                
            