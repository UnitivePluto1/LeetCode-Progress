class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        Max = 0

        while left < right:
            area = (right-left)*min(height[left],height[right])
            Max = max(Max,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return Max
            
            
