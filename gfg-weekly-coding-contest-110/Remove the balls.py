from typing import List

class Solution:
    # Version 1: Stack
    # TC: O(n), SC: O(n)
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        stack = []
        for i in range(N):
            if stack and color[stack[-1]] == color[i] and radius[stack[-1]] == radius[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
