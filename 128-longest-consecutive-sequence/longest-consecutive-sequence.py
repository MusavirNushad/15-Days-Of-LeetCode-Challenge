class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums.sort()
        
        maxL = 1
        length = 1

        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                length+=1
            elif nums[i-1] == nums[i]:
                continue
            else:
                 maxL = max(length, maxL)
                 length =1
        
        maxL = max(length, maxL)
               
            
        
        return maxL
    