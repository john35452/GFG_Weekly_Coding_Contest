

//User function Template for Java
class Solution{
    // Version 1: Store time point and diff array
    // Store two points for each interval
    // TC: O(nlogn), SC: O(n)
    public static int powerfullInteger(int n,int interval[][],int k)
    {
        TreeMap<Integer, Integer> diff = new TreeMap<>();
        for (int[] pair: interval) {
            diff.put(pair[0], diff.getOrDefault(pair[0], 0) + 1);
            diff.put(pair[1] + 1, diff.getOrDefault(pair[1] + 1 , 0) - 1);
        }
        
        int current = 0;
        int ans = -1;
        for (Map.Entry<Integer, Integer> pair: diff.entrySet()) {
            if (pair.getValue() > 0) {
                current += pair.getValue();
                if (current >= k) {
                    ans = pair.getKey();
                }
            } else {
                if (current >= k) {
                    ans = pair.getKey() - 1;
                } 
                current += pair.getValue();
            }
        }
        return ans;
    }
}