#User function Template for python3
class Solution:
    # Version 1: Put vowel at position k - 1 and also every k gap
    # TC: O(n), SC: O(n)
    '''
    def construct(self, N, K): 
        #code here
        s = ['z']*N
        i = K - 1
        while i < N:
            s[i] = 'a'
            i += K
        return ''.join(s)
    '''
    
    # Version 2: Greedy
    # Since k >= 2, we can have a string with alternating vowels and consonants
    # TC: O(n), SC: O(n)
    def construct(self, N, K): 
        #code here
        res = []
        for i in range(N):
            if i % 2 > 0:
                res.append('a')
            else:
                res.append('b')
        return ''.join(res)
    