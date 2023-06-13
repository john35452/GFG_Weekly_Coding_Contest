

//User function Template for Java

class Solution
{
    // Version 1: Check the times of A
    // TC: O(B/A), SC: O(B/A)
    public static ArrayList<Long> allNumbers(long A,long B)
    {
        ArrayList<Long> ans = new ArrayList<>();
        for (long i = 1; i <= B/A; i++) {
            if (B % (i * A) == 0) {
                ans.add(i * A);
            }
        }
        return ans;
    }
}