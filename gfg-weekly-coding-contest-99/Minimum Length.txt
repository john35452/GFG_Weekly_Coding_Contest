from typing import List


class Solution:
    # Version 1: Sliding window
    # Count the extra frequency and get the smallest subarray for this.
    # TC: O(n), SC: O(n)
    def minLength(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        from collections import Counter
        fre = Counter(arr)
        target = {}
        for key in fre:
            if fre[key] > k:
                target[key] = fre[key] - k
        match = 0
        i = 0
        j = 0
        ans = float('inf')
        current = {}
        while i < n and match < len(target):
            if arr[i] not in current:
                current[arr[i]] = 0
            current[arr[i]] += 1
            if arr[i] in target and current[arr[i]] == target[arr[i]]:
                match += 1
            i += 1
            if match == len(target):
                while j < i and match == len(target):
                    if arr[j] in target and current[arr[j]] == target[arr[j]]:
                        match -= 1
                    current[arr[j]] -= 1
                    if not current[arr[j]]:
                        current.pop(arr[j])
                    j += 1
                ans = min(ans, i - j + 1)
        return ans if ans != float('inf') else 0
