

//User function Template for Java
class Solution 
{ 
    // Version 1: Dijkstra
    // Store two kinds of dis and graph
    // TC: O(VlogE), SC: O(E + V)
    /*
    long minTime(int N, int X, int src, int dest, int M1, int M2, int airlines[][], int railways[][]) 
    {
        // code here 
        Long[] dis_a = new Long[N];
        Long[] dis_t = new Long[N];
        List<Map<Integer, Long>> graph_a = new ArrayList<>(N);
        List<Map<Integer, Long>> graph_t = new ArrayList<>(N);
        
        for (int i = 0; i < N; i++) {
            graph_a.add(new HashMap<Integer, Long>());
            graph_t.add(new HashMap<Integer, Long>());
        }
        
        for (int i = 0; i < M1; i++) {
            graph_a.get(airlines[i][0]).put(airlines[i][1], (long)airlines[i][2]);
        }
        
        for (int i = 0; i < M2; i++) {
            graph_t.get(railways[i][0]).put(railways[i][1], (long)railways[i][2]);
        }
        
        PriorityQueue<long[]> pq = new PriorityQueue<long[]>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[] {0, src, 0});
        pq.offer(new long[] {0, src, 1});
        
        while (!pq.isEmpty()) {
            long[] item = pq.poll();
            if ((item[2] == 0 && dis_a[(int)item[1]] == null) || (item[2] == 1 && dis_t[(int)item[1]] == null)) {
                if (item[2] == 0) {
                    dis_a[(int)item[1]] = item[0];
                } else {
                    dis_t[(int)item[1]] = item[0];
                }
                for (Map.Entry<Integer, Long> entry: graph_a.get((int)item[1]).entrySet()) {
                    if (dis_a[entry.getKey()] == null) {
                        long transfer = (item[2] == 1)? X:0;
                        pq.offer(new long[] {item[0] + entry.getValue() + transfer, entry.getKey(), 0});
                    }
                }
                for (Map.Entry<Integer, Long> entry: graph_t.get((int)item[1]).entrySet()) {
                    if (dis_t[entry.getKey()] == null) {
                        long transfer = (item[2] == 0)? X:0;
                        pq.offer(new long[] {item[0] + entry.getValue() + transfer, entry.getKey(), 1});
                    }
                }
            }
        }
        
        if (dis_a[dest] == null && dis_t[dest] == null) {
            return -1;
        } else {
            return Math.min(dis_a[dest] == null? Long.MAX_VALUE :dis_a[dest], dis_t[dest] == null? Long.MAX_VALUE : dis_t[dest]);
        }
    }
    */
    
    // Version 2: Dijkstra
    // Set the N cities to 2N cities and separate the used transportation.
    // TC: O(VlogE), SC: O(E + V)
    long minTime(int N, int X, int src, int dest, int M1, int M2, int airlines[][], int railways[][]) 
    {
        // code here 
        Long[] dis = new Long[2*N];
        List<Map<Integer, Long>> graph = new ArrayList<>(2*N);
        
        for (int i = 0; i < 2*N; i++) {
            graph.add(new HashMap<Integer, Long>());
        }
        
        for (int i = 0; i < M1; i++) {
            graph.get(N + airlines[i][0]).put(N + airlines[i][1], (long)airlines[i][2]);
        }
        
        for (int i = 0; i < M2; i++) {
            graph.get(railways[i][0]).put(railways[i][1], (long)railways[i][2]);
        }
        
        for (int i = 0; i < N; i++) {
            graph.get(i).put(i + N, (long)X);
            graph.get(i + N).put(i, (long)X);
        }
        
        PriorityQueue<long[]> pq = new PriorityQueue<long[]>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[] {0, src});
        pq.offer(new long[] {0, src+N});
        
        while (!pq.isEmpty()) {
            long[] item = pq.poll();
            if (dis[(int)item[1]] == null) {
                dis[(int)item[1]] = item[0];
                for (Map.Entry<Integer, Long> entry: graph.get((int)item[1]).entrySet()) {
                    if (dis[entry.getKey()] == null) {
                        pq.offer(new long[] {item[0] + entry.getValue(), entry.getKey()});
                    }
                }
            }
        }
        
        if (dis[dest] == null && dis[dest + N] == null) {
            return -1;
        } else {
            return Math.min(dis[dest] == null? Long.MAX_VALUE :dis[dest], dis[dest + N] == null? Long.MAX_VALUE : dis[dest + N]);
        }
    }
} 