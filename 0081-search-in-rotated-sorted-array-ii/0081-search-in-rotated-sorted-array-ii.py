class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0 
        ryt = len(nums) - 1

        while left <= ryt :
            mid = left + (ryt - left ) // 2

            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[ryt]:
                left += 1
                ryt -= 1
                continue
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    ryt = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[ryt]:
                    left = mid + 1
                else:
                    ryt = mid - 1
        return False
