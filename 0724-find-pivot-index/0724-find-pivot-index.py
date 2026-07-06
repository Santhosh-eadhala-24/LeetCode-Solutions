class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rytSum = totalSum - leftSum - nums[i]

            if leftSum == rytSum:
                return i
            leftSum += nums[i]
        return -1