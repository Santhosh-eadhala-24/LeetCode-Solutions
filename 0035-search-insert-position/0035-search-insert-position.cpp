class Solution {
public:
    int searchInsert(vector<int>& nums, int target) 
    {
        int left=0;
        int n=nums.size();
        int ryt=nums.size() - 1;
        int mid;
        while(left <= ryt)
        {
            mid=left + (ryt - left)/2;

            if(target > nums[mid])
                left=mid+1;

            else if(target < nums[mid])
                ryt=mid-1;
            
            else 
                return mid;
        }
        return left;
    }
};