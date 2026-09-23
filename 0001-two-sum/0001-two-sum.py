class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                summ = nums[i] + nums[j]
                if summ == target:
                    return i,j

        return -1,-1

            