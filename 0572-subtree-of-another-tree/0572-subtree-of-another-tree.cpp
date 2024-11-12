/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        //if subroot is null its always a subtree
        if (!subRoot){
            return true;
        }
        // if root is null and subroot is not then its never subtree
        if (!root){
            return false;
        }
        // check recursively if they are identical trees
        if (sameTree(root, subRoot)){
            return true;
        }
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

        bool sameTree(TreeNode* root, TreeNode* subRoot){
            if(!root && !subRoot){
                return true;
            }
            if(root && subRoot && root -> val == subRoot -> val){
                return sameTree(root->left, subRoot->left) && sameTree(root->right, subRoot->right);
            }
            return false;
        }

    
};
