//User function Template for C++

/*
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
*/
class Solution{
public:
    // This is the same question as binary tree cameras on Leetcode
    // https://leetcode.com/problems/binary-tree-cameras/
    // Version 1: Greedy
    // Use post traversal and supply vaccine when needed.
    // TC: O(n), SC: O(n)
    /*
    int supplyVaccine(Node* root){
        // code here
        unordered_set<Node*> covered;
        vector<int> ans;
        covered.insert(NULL);
        ans.push_back(0);
        dfs(root, NULL, covered, ans);
        return ans[0];
    }
    
    void dfs(Node* node, Node* parent, unordered_set<Node*>& covered, vector<int>& ans) {
        if (!node) return;
        dfs(node->left, node, covered, ans);
        dfs(node->right, node, covered, ans);
        if (covered.find(node->left) == covered.end() || 
            covered.find(node->right) == covered.end() || 
            (!parent && covered.find(node) == covered.end())
        ) {
            ans[0]++;
            covered.insert(node->left);
            covered.insert(node->right);
            covered.insert(node);
            covered.insert(parent);
        }
    }
    */
    
    // Version 2: Return the state of the subtree
    // 0: root covered but no camera
    // 1: root covered and with camera
    // 2: root not covered
    // TC: O(n), SC: O(1)
    int supplyVaccine(Node* root){
        // code here
        vector<int> ans;
        ans.push_back(0);
        if (dfs(root, ans) > 1) ans[0]++;
        return ans[0];
    }
    
    int dfs(Node* node, vector<int>& ans) {
        if (!node) return 0;
        int left = dfs(node->left, ans);
        int right = dfs(node->right, ans);
        if (left == 2 || right == 2) {
            ans[0]++;
            return 1;
        } else if (left == 1 || right == 1) {
            return 0;
        } else {
            return 2;
        }
    }
};