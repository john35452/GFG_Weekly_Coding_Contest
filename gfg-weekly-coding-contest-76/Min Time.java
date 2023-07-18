

class Solution {
    // Version 1: DP
    // There are mutliple same type fruits at different locations
    // Therefore, we only care about the most leftest and rightest position.
    // We can use dp to calculate the cost to reach leftest and rightest position.
    // TC: O(nlogn), SC: O(n)
    public static long minTime(int n, int[] locations, int[] types) {
        // code here
        int left_pos = 0, right_pos = 0;
        long left = 0L, right = 0L;
        TreeMap<Integer, int[]> fruit = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            fruit.putIfAbsent(types[i], new int[] {locations[i], locations[i]});
            int[] loc = fruit.get(types[i]);
            loc[0] = Math.min(loc[0], locations[i]);
            loc[1] = Math.max(loc[1], locations[i]);
            fruit.put(types[i], loc);
        }
        
        for (Map.Entry<Integer, int[]> entry: fruit.entrySet()) {
            int[] pos = entry.getValue();
            long middle = pos[1] - pos[0];
            long new_left, new_right;
            new_left = Math.min(right + Math.abs(pos[1] - right_pos), 
                                left + Math.abs(pos[1] - left_pos)) 
                        + middle;
            new_right = Math.min(right + Math.abs(pos[0] - right_pos), 
                                left + Math.abs(pos[0] - left_pos)) 
                        + middle;
            left_pos = pos[0];
            right_pos = pos[1];
            left = new_left;
            right = new_right;
        }
        return Math.min(left + Math.abs(left_pos), right + Math.abs(right_pos));
    }
}
        