

//User function Template for Java

class GFG{
    
    // Version 1: Store last submission
    // TC: O(n), SC: O(n)
    int gap;
    Map<String, Integer> user;
    
    public GFG(int cap){
        // Constructor
        this.gap = cap;
        this.user = new HashMap<>(); 
        
    }
    public boolean judgeOrNot(String submissionId){
        // Complete the function.  
        String[] submission = submissionId.split("@");
        String[] t = submission[1].split(":");
        int time = 0;
        int base = 1;
        for (int i = 2; i >= 0; i--) {
            time += Integer.valueOf(t[i]) * base;
            base *= 60;
        }
        
        if (this.user.containsKey(submission[0])) {
            int last_t = this.user.get(submission[0]);
            int diff = 0;
            if (time >= last_t) {
                diff = time - last_t;
            } else {
                diff = 86400 - last_t + time;
            }
            if (diff < this.gap) {
                return false;   
            }
        } 
        this.user.put(submission[0], time);
        return true;                    
    }
    
}