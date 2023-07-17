class Solution:
    # Version 1: Count
    # TC: O(n), SC: O(1)
    '''
    def maxInstance(self, s : str) -> int:
        # code here
        from collections import Counter
        fre = {}
        for c in s:
            if c not in fre:
                fre[c] = 0
            fre[c] += 1
        ans = 0
        balloon = Counter("balloon")
        while fre:
            done = False
            for c, v in balloon.items():
                if c not in fre or fre[c] < v:
                    done = True
                    break
                fre[c] -= v
            if done:
                break
            ans += 1
        return ans
    '''
    
    # Version 2: Improved version 1
    # TC: O(n), SC: O(1)
    def maxInstance(self, s : str) -> int:
        # code here
        from collections import Counter
        fre = Counter(s)
        ans = float('inf')
        balloon = Counter("balloon")
        for k, v in balloon.items():
            ans = min(ans, fre[k] // v)
        return ans if ans != float('inf') else 0
