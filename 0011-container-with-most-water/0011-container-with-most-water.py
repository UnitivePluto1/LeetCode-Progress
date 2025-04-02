class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0, len(height) - 1
        waterArea = 0
        while i < j:
            mm = min(height[i], height[j])
            waterArea = max(waterArea,mm*abs(i-j))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return waterArea