from typing import List


class Solution:
    # Version 1: Greedy
    # Do the most beneficial works first
    # Sort the query to fill in the value greedly
    # TC: O(nlogn + qlogq), SC: O(n + q)
    '''
    def findMin(self, n : List[int],q : List[int], gain : List[int], loss : List[int], query : List[int]) -> List[int]:
        # code here
        earn = [gain[i] - loss[i] for i in range(n)]
        earn.sort(reverse=True)
        query = [(query[i], i) for i in range(q)]
        query.sort()
        ans = [-1]*q
        current = 0
        j = 0
        for i in range(n):
            current += earn[i]
            while j < q and current >= query[j][0]:
                ans[query[j][1]] = i + 1
                j += 1
        return ans
    '''

    # Version 2: Binary Search
    # TC: O(nlogn + qlogn), SC: O(n)
    def findMin(self, n : List[int],q : List[int], gain : List[int], loss : List[int], query : List[int]) -> List[int]:
        from bisect import bisect_left
        earn = []
        for i in range(n):
            if loss[i] < gain[i]:
                earn.append(gain[i] - loss[i])
        earn.sort(reverse=True)
        for i in range(1, len(earn)):
            earn[i] += earn[i - 1]
        ans = [-1]*q
        for i in range(q):
            val = query[i]
            index = bisect_left(earn, val)
            if index < len(earn):
                ans[i] = index + 1
        return ans
        