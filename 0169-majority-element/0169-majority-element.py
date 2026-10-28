class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                a = nums[i]

            if nums[i] == a:
                cnt += 1
            else:
                cnt -= 1

        return a