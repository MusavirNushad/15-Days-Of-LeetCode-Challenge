class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        countDup = {}

        for num in nums:
            if num in countDup:
                countDup[num] += 1
            else:
                countDup[num] = 1
        
        for k in nums:
            if countDup[k] > 1:
                return True
        
        return False