#include<bits/stdc++.h>
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) 
    {
        unordered_set<int> hs(nums1.begin(),nums1.end());
        unordered_set<int> res;

        for( auto i : nums2)
        {
            if(hs.count(i))
            {
                res.insert(i);
            }
        }
        return vector<int>(res.begin(),res.end());
    }
};