from typing import List


class Solution:
    # Version 1: Store the cheapest price for each item
    # TC: O(n), SC: O(n)
    def antiqueItems(self, n : int, items : List[int], price : List[int]) -> int:
        # code here
        p = {}
        for i in range(n):
            p[items[i]] = min(p.get(items[i], float('inf')), price[i])
        return sum(p.values())
        
