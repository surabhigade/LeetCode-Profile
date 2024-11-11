class Solution {
public:
    bool isPalindrome(int x) {
        string y = to_string(x);
        int m; int i;
        m = y.size();
        for (i=0; i<m/2; i++ ) {
            if (y[i] != y[m-1-i]) {
               return false;
            } 
        }
        return true;
    }
};