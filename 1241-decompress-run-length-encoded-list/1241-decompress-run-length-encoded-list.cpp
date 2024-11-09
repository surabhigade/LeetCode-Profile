#include <iostream>
#include <vector>
using namespace std;

class Solution 
{
public:
    vector<int> decompressRLElist(vector<int>& nums) 
    {
        // Calculate the size of the nums vector
        int m = nums.size(); 
        // The resulting decompressed vector
        vector<int>array;

        // Iterate through the nums vector
        for(int i=0; i < m; i+=2)
        {
            int freq = nums[i];
            int value = nums[i+1];
            
            //Add 'freq' copies of value to the result
            for (int j=0; j<freq; j++)
            {
                array.push_back(value);
            }
        }
        return array;
    }
};
