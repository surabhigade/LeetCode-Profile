class Solution {
public:
    bool isPalindrome(string s) {
    // Initialize the pointers, one at the beginning and one at the end of the string
    int l= 0, r = s.length()-1;
    // Continue until the two pointers meet at the middle
    while (l<r){
        // move the left pointer to the right, skipping non alphanumeric characters
        while(l<r && !alphaNum(s[l])){
            l++;
        }
        // move the right pointer to the left, skipping non alphanumeric characters
        while(l<r && !alphaNum(s[r])){
            r--;
        }
        // compare characters, ignoring case differences
        if(tolower(s[l]) != tolower(s[r])){
            return false;
        }
        // move both pointers towards the center
        l++; r--;
    }
    // if all the characters matched, its a palindrome
    return true;
    }

    bool alphaNum(char c){
        return (c >='A' && c<= 'Z') || (c >='a' && c<= 'z') || (c >='0' && c<= '9');     
    }
};
