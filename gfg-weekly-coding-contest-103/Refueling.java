

//User function Template for Java

class Solution{
    // Version 1: Choose the closest position
    // TC: O(logn), SC: O(1) 
    public long refueling(int X){
        // Code your solution here. 
        long ans = 1;
        while (ans < X) {
            ans <<= 1;
        }
        if (X - (ans >> 1) < ans - X) {
            return ans >> 1;
        } else {
            return ans;
        }
    }
}