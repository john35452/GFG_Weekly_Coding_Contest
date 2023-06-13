

//User function Template for Java
class Solution
{
    // Version 1: Calculate the LCM and check every part of them(TLE)
    // However, if both A and B are prime, we need to check min(A, B) times
    // TC: O(min(A, B)), SC: O(1)
    /*
    public static int longestSubarray(int A,int B)
    {
        int g = gcd(A, B);
        long lcm = 1L * A * B / g;
        int minv = Math.min(A, B);
        int maxv = Math.max(A, B);
        int count = 1;
        int ans = 0;
        long[] index = {1L, 1L};
        while (maxv * index[1] <= lcm) {
            long left = maxv * index[1];
            long right = maxv * (index[1] - 1);
            ans = Math.max(ans, (int)(left / minv - (left % minv == 0 ?1: 0) - right / minv));
            index[1]++;
        }
        return ans;
    }
    
    public static int gcd(int a, int b) {
        if (b == 0) return a;
        else return gcd(b, a % b);
    }
    */
    
    // Version 2: Math
    // Let say A > B, between every two times of A.
    // The nearest distance between first B and first A is gcd(A, B)
    // Then we can calculate the longest subarray
    // TC: O(log(max(A, B))), SC: O(1)
    public static int longestSubarray(int A,int B)
    {
        //int g = gcd(A, B);
        //A /= g;
        //B /= g;
        int g = gcd(A, B);
        if (B > A) {
            int tmp = A;
            A = B;
            B = tmp;
        }
        int ans = 1;
        A -= g;
        ans += A / B;
        if (A % B == 0 && A > 0) ans--;
        return ans;
    }
    
    public static int gcd(int a, int b) {
        if (b == 0) return a;
        else return gcd(b, a % b);
    }
}