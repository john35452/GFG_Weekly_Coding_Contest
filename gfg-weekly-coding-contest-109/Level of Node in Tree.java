

class Solution{
    // Version 1: Count
    // TC: O(logn) = O(1), SC: O(1)
    public long FindLevel(long N) {
        // Code Here.
        long cur = 1;
        long level = 1;
        long count = 0;
        while (count < N) {
            count += cur;
            cur *= (level + 1);
            level++;
        }
        return level - 1;
    }
}