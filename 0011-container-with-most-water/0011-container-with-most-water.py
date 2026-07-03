class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        ryt = len(height)-1
        mArea = 0
        while( left <= ryt):
            hei = min(height[left],height[ryt])
            wid = ryt - left
            area = hei * wid
            mArea = max(mArea,area)

            if height[left] <= height[ryt]:
                left += 1
            else:
                ryt -= 1
        return mArea