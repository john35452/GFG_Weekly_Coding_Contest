

//User function Template for Java

class Solution{
    // Version 1: Check whether 2^k in the range
    // Since 2^k can contribute to the kth bit in binary representation.
    // Among all numbers can contribute to kth bit, 2^k is also the smallest number.
    // TC: O(logn), SC: O(1)
    public int rangeOR(int n){
        // Code here. 
        int ans = 0;
        int base = 1;
        while (base <= n) {
            ans |= base;
            base <<= 1;
        }
        return ans;
    }
}