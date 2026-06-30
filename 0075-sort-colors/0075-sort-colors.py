class Solution:
    def swap(self,nums,i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while(mid <= high):
            if nums[mid] == 0:
                self.swap(nums,low,mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(nums,mid,high)
                high -= 1
        