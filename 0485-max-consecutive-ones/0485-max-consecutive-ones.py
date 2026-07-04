class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        j = 0 
        n = len(nums)
        cc = 0
        maxi = 0
        while j < n:
            if nums[j] == 1:
                cc += 1
            else :
                maxi = max(maxi, cc)
                cc = 0
            j += 1
        return max(maxi,cc)