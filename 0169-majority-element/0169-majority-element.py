class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        cunt = 0
        for i in range(n):
            if cunt == 0:
                cunt = 1
                ele = nums[i]

            elif nums[i] == ele :
                cunt += 1
            
            else:
                cunt -= 1

        cunt1 = 0

        for i in range(n):
            if nums[i] == ele:
                cunt1 += 1

        if cunt1 > n/2:
            return ele

        
