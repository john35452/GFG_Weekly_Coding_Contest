
class Solution:
    # Version 1: Count 1 in binary representation
    # TC: O(logn), SC: O(logn)
    def nBlocks(self, w : int) -> int:
        # code here
        bw = bin(w)[2:]
        return bw.count('1')
        