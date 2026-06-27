class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxi=0,cunt=0;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            if(nums[i] == 1)
            {
                cunt++;
                maxi=max(maxi,cunt);
            }
            else
            {
                cunt=0;
            }
        }
        return maxi;
    }

};