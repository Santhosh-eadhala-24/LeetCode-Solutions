class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0

        for i in range(len(nums)):
            if(nums[i] != 0):
                tmp = nums[i]
                nums[i]=nums[l]
                nums[l]=tmp
                l+=1
        