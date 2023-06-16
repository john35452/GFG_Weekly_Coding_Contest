// User function Template for C++

class Solution
{
public:
    long long bigMod(long long a, long long b, long long M)
    {
        if (b == 0)
            return 1;
        long long half = bigMod(a, b / 2, M);
        long long res = (half * half) % M;
        if (b % 2 > 0)
        {
            res = (res * a) % M;
        }
        return res;
    }

    // Version 1: Store the frequency of each alphbet
    // TC: O(n + 26k) = O(n + k), SC: O(n)
    /*
    int maximumPossible(int n,int k,string s)
    {
        //code here
        vector<int> fre(26, 0);
        for (int i = 0; i < n; i++) fre[s[i] - 'a']++;
        long long M = 1e9 + 7;

        for (int i = 0; i < k; i++) {
            int max_f = 0, min_f = 0;
            for (int j = 0; j < 26; j++) {
                if (fre[j] > fre[max_f]) max_f = j;
                if (fre[j] < fre[min_f]) min_f = j;
            }

            if (fre[max_f] - fre[min_f] <= 1) break;

            fre[max_f]--;
            fre[min_f]++;
        }

        long long fac[n + 1] = {0};
        fac[0] = 1;
        for (int i = 1; i <= n; i++) {
            fac[i] = (fac[i - 1] * i) % M;
        }

        long long ans = fac[n];
        for (int i = 0; i < 26; i++) {
            if (fre[i] > 1) {
                ans = (ans * bigMod(fac[fre[i]], M - 2, M)) % M;
            }
        }
        return (int)ans;
    }
    */

    // Version 2: Use min and max heap to get the max and min frequency alphbet
    // TC: O(n + k log26) = O(n + k), SC: O(n)
    /*
    int maximumPossible(int n,int k,string s)
    {
        //code here
        vector<int> fre(26, 0);
        for (int i = 0; i < n; i++) fre[s[i] - 'a']++;
        long long M = 1e9 + 7;
        priority_queue<pair<int, int>> maxv;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minv;

        for (int i = 0; i < 26; i++) {
            maxv.push({fre[i], i});
            minv.push({fre[i], i});
        }

        for (int i = 0; i < k; i++) {
            while (!maxv.empty() && maxv.top().first != fre[maxv.top().second]) {
                maxv.pop();
            }

            while (!minv.empty() && minv.top().first != fre[minv.top().second]) {
                minv.pop();
            }

            pair<int, int> item_max = maxv.top();
            pair<int, int> item_min = minv.top();
            maxv.pop();
            minv.pop();
            if (item_max.first - item_min.first <= 1) break;

            fre[item_max.second]--;
            fre[item_min.second]++;
            item_max.first--;
            item_min.first++;
            maxv.push(item_max);
            maxv.push(item_min);
            minv.push(item_max);
            minv.push(item_min);
        }

        long long fac[n + 1] = {0};
        fac[0] = 1;
        for (int i = 1; i <= n; i++) {
            fac[i] = (fac[i - 1] * i) % M;
        }

        long long ans = fac[n];
        for (int i = 0; i < 26; i++) {
            if (fre[i] > 1) {
                ans = (ans * bigMod(fac[fre[i]], M - 2, M)) % M;
            }
        }
        return (int)ans;
    }
    */

    // Version 3: Use multiset for maximum and minimum frequency choosing
    // TC: O(n + k log 26) = O(n + k), SC: O(n)
    int maximumPossible(int n, int k, string s)
    {
        // code here
        vector<int> fre(26, 0);
        for (int i = 0; i < n; i++)
            fre[s[i] - 'a']++;
        long long M = 1e9 + 7;
        multiset<int> fre_value;

        for (int i = 0; i < 26; i++)
        {
            fre_value.insert(fre[i]);
        }

        for (int i = 0; i < k; i++)
        {
            int minf = *fre_value.begin();
            int maxf = *fre_value.rbegin();
            if (maxf - minf <= 1)
                break;

            fre_value.erase(fre_value.find(minf));
            fre_value.erase(fre_value.find(maxf));
            minf++;
            maxf--;
            fre_value.insert(minf);
            fre_value.insert(maxf);
        }

        long long fac[n + 1] = {0};
        fac[0] = 1;
        for (int i = 1; i <= n; i++)
        {
            fac[i] = (fac[i - 1] * i) % M;
        }

        long long ans = fac[n];
        for (int val : fre_value)
        {
            if (val > 1)
            {
                ans = (ans * bigMod(fac[val], M - 2, M)) % M;
            }
        }
        return (int)ans;
    }
};