#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        int m = nums.size();
        // Outer loop to sort elements at odd indices sorted
        for(int i=1; i< m; i += 2){
            // Last i elements are already sorted 
            for (int j=1; j<m-2; j +=2){
                //comparing the adjacent elements
                if(nums[j] < nums[j+2]){
                    swap(nums[j], nums[j+2]);
                }
            }
           
        }

        // Outer loop to sort elements at even indices 
        for(int i=0; i< m; i += 2){
            // Last i elements are already sorted 
            for (int j=0; j< m-2; j +=2){
                //comparing the adjacent elements
                if(nums[j] > nums[j+2] ){
                    swap(nums[j], nums[j+2]);
                }
            }   
        }
        return nums;
    }
};