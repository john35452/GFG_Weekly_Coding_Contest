from typing import List


class Solution:
    # Version 1: DP
    # There are mutliple same type fruits at different locations
    # Therefore, we only care about the most leftest and rightest position.
    # We can use dp to calculate the cost to reach leftest and rightest position.
    # TC: O(nlogn), SC: O(n)
    def minTime(self, n : int, locations : List[int], types : List[int]) -> int:
        # code here
        pos = {}
        for i in range(n):
            if types[i] not in pos:
                pos[types[i]] = [locations[i], locations[i]]
            pos[types[i]][0] = min(pos[types[i]][0], locations[i])
            pos[types[i]][1] = max(pos[types[i]][1], locations[i])
        ts = sorted(pos.keys())
        left = right = 0
        left_pos = right_pos = 0
        for t in ts:
            middle = pos[t][1] - pos[t][0]
            nextLeft = min(abs(pos[t][1] - left_pos) + left, abs(pos[t][1] - right_pos) + right) + middle
            nextRight = min(abs(pos[t][0] - left_pos) + left, abs(pos[t][0] - right_pos) + right) + middle
            left_pos, right_pos = pos[t]
            left, right = nextLeft, nextRight
        return min(left + abs(left_pos), right + abs(right_pos))
