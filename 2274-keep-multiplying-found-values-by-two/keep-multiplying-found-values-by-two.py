class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        mapnum = {}

        for num in nums:
            if num not in mapnum:
                mapnum[num] = num
        
        res = original
        for numb in nums:
            if res in mapnum:
                res*=2
            else:
                return res
        
        return res

