class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
       int m; int i;
        m = nums.size();
        i = 0;
        bool found = true; //falg to check if we found the original
        // Loop over array to find original
        while(found){
            found = false;  // reset the found flag for this iteration
            for(i=0; i<m; i += 1){
                if (original == nums[i])
                {
                    original = 2* original; // double the value
                    found = true; // set flag true if we found the original
                    break; // exit loop since we found it
                }
            }
        }
        return original;            
    }
};