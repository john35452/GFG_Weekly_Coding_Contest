

//User function Template for Java

class Solution{
    // Version 1: Divide into two side
    // Check the common characters
    // TC: O(26n) = O(n), SC: O(26) = O(1)
    public int splitString(int n, String s){
        // Code Here.
        int[] left = new int[26];
        int[] right = new int[26];
        for (int i = 0; i < n; i++) {
            right[s.charAt(i) - 'a']++;
        }
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            left[s.charAt(i) - 'a']++;
            right[s.charAt(i) - 'a']--;
            int common = 0;
            for (int j = 0; j < 26; j++) {
                if (left[j] > 0 && right[j] > 0) {
                    common++;
                }
            }
            ans = Math.max(ans, common);
        }
        return ans;
    }
    
}