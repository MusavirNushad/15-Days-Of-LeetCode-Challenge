class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height)-1

        maxWater = 0
        while i < j:
            multfactor = min(height[i], height[j])

            currWater = multfactor*(j-i)
            maxWater = max(maxWater, currWater)
            
            if height[i] > height[j]:
                j-=1
            elif height[i] < height[j]:
                i+=1
            else:
                i+=1
        
        return maxWater