class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums) 
        posIdx = 0
        negIdx = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                res[negIdx] = nums[i]
                negIdx += 2
            else:
                res[posIdx] = nums[i]
                posIdx += 2
        return res