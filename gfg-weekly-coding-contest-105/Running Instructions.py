
from typing import List


class Solution:
    # Version 1: BFS
    # TC: O(len(k)), SC: O(len(k))
    def instructionCheck(self, m : int, n : int, k : List[int]) -> str:
        # code here
        current = set([0])
        for i in range(n):
            nextStep = set()
            while current:
                val = current.pop()
                nextStep.add((val + k[i]) % m)
                nextStep.add((val - k[i]) % m)
            current, nextStep = nextStep, current
            
        if 0 in current:
            return "YES"
        else:
            return "NO"