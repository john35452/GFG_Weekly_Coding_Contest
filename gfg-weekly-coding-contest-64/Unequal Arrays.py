

from typing import List
class Solution:
    # Version 1: Greedy
    # If A can be swap to B, it means sum(A) == sum(B)
    # Since every operation cause a difference of 2, the number of odd and even numbers also need to be the same.
    # For the swapping part, it's also possible to add even number and subtract odd number.
    # We just need to know how many add and sub is needed to make A same as B.
    # TC: O(nlogn), SC: O(n)
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        A.sort()
        B.sort()
        dataA = [[], []]
        dataB = [[], []]
        total = 0
        for k in A:
            total += k
            dataA[k % 2].append(k)
        for k in B:
            total -= k
            dataB[k % 2].append(k)
        if len(dataA[0]) != len(dataB[0]) or total != 0:
            return -1
        add = 0
        sub = 0
        for k in range(2):
            for i in range(len(dataA[k])):
                diff = dataB[k][i] - dataA[k][i]
                if diff > 0:
                    add += diff // 2
                else:
                    sub += diff // 2
        return add
