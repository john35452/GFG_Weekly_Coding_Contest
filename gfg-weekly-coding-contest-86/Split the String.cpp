// User function Template for C++

class Solution
{
public:
	// Version 1: Divide into two side
	// Check the common characters
	// TC: O(26n) = O(n), SC: O(26) = O(1)
	int splitString(int n, string s)
	{
		// code here
		vector<int> left(26, 0);
		vector<int> right(26, 0);
		for (int i = 0; i < n; i++)
		{
			right[s[i] - 'a']++;
		}

		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			left[s[i] - 'a']++;
			right[s[i] - 'a']--;
			int common = 0;
			for (int j = 0; j < 26; j++)
			{
				if (left[j] > 0 && right[j] > 0)
					common++;
			}
			ans = max(ans, common);
		}
		return ans;
	}
};