#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int fillCups(vector<int>& amount) {
       int m = amount.size();
       int seconds = 0;

       while(amount[0]>0 || amount[1]>0 || amount[2]>0){
        sort(amount.begin(), amount.end(), greater<int>());
            if (amount[0]>0 || amount[1]>0){
                amount[0]--;
                amount[1]--;
            }
            else if (amount[0] > 0){
                amount[0] --;
            }
            seconds++;
        }
    return seconds;   
    }
};