

class Solution {
    // Version 1: Greedy
    // To get the smallest string, we would like to get the longest descending prefix.
    // However, there is a case to have consecutive same alphbet.
    // If the prefix only contains one alphbet, we only take one character.
    // For other case, we can take all of them.
    // TC: O(n), SC: O(n)
    public static String stringMirror(String str) {
        // code here
        int i = 1;
        int n = str.length();
        boolean hasGreater = false;
        while (i < n) {
            if (str.charAt(i) < str.charAt(i - 1)) {
                hasGreater = true;
            } else if (str.charAt(i) == str.charAt(i - 1) && hasGreater) {
                hasGreater = true;
            } else {
                break;
            }
            i++;
        }
        StringBuilder prefix = new StringBuilder(str.substring(0, i));
        StringBuilder ans = new StringBuilder(prefix);
        prefix.reverse();
        ans.append(prefix);
        return ans.toString();
    }
}