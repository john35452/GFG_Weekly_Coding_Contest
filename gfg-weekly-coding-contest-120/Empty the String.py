#User function Template for python3

class Solution:
    # Version 1: Stack
    # TC: O(n), SC: O(n)
    def makeStringEmpty(self, s):
        # code here 
        ans = 0
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) > 3 and ''.join(stack[-4:]) == "geek":
                for _ in range(4):
                    stack.pop()
                ans += 1
        return ans if not stack else -1