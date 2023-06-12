

//User function Template for Java

class Solution{
    // Version 1: Greedy
    // The lexicographically smallest array happen when a starts from the biggest numbers.
    // TC: O(nlogn), SC: O(n)
    public int[] mexArray(int n, int a[]){
        // Code Here.
        Arrays.sort(a);
        int[] ans = new int[n];
        int miss = 0;
        Set<Integer> current = new HashSet<>();
        for (int i = 0; i < n; i++) {
            current.add(a[n - 1 - i]);
            while (current.contains(miss)) {
                miss++;
            }
            ans[i] = miss;
        }
        return ans;
    }
}