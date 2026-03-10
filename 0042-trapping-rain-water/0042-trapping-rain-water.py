class Solution:
    def trap(self, height: List[int]) -> int:
        n, m = 0, len(height)-1
        leftMax, rightMax = height[0], height[m]
        tot = 0

        while n < m:
            if leftMax < rightMax:
                n+=1
                leftMax = max(leftMax, height[n])
                tot += leftMax - height[n]
            else:
                m-=1
                rightMax= max(rightMax, height[m])
                tot+= rightMax - height[m]

        # for i in range(0,m):

        #     rightMax[i] += max(height[i:])
        #     leftMax[-i-1] += max(height[(-i-1)::-1])
        
        # for j in range(len(height)):
        #     cap = min(rightMax[j],leftMax[j]) - height[j]

        #     tot += cap

        return tot
