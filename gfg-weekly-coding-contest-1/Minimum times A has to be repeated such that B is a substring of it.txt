#User function Template for python3

class Solution:
    # Same Leetcode problem:
    # https://leetcode.com/problems/repeated-string-match/
    
    
    # Version 1: Find the matching point and length
    # TC: O(mn), SC: O(1)
    '''
    def minRepeats(self, A, B):
        # code here
        
        m = len(A)
        n = len(B)
        if m > n:
            return -1
        ans = float('inf')
        
        for s in range(m):
            i = s
            j = 0
            match = 0
            while A[i] == B[j] and match < n:
                i = (i + 1) % m
                j = (j + 1) % n
                match += 1
            if match == n:
                ans = min(ans, 1 + (n - (m - s)) // m + int((n - (m - s)) % m > 0))
        return ans if ans != float('inf') else -1
    '''
    
    # Version 2: Only 2 cases are possible
    # If string b can be a substring of repeated string a,
    # String b can be divided into s1, s2, s3.
    # s1 is the suffix of string a
    # s2 is k copy of string a (k >= 0)
    # s3 is the prefix of string a
    # It's possible that only s1 or s2 or s3 is non-empty.
    # But in order to know whether string b is in repeated string a.
    # We can copy string a multiple time to c until len(c) >= len(b), which makes c covers s1, s2.
    # In order to cover all case, we also need to add one more string a to c to cover s1, s2, and s3. 
    # Therefore, we only need to check two cases.
    # TC: O(n + m), SC: O(n + m)
    def minRepeats(self, A, B):
        tmp = A
        while len(A) < len(B):
            A = A + tmp
        for t in range(2):
            if B in A:
                return len(A) // len(tmp)
            A = A + tmp
        return -1