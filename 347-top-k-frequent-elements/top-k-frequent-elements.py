class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}

        for num in nums:
            if num not in mp:
                mp[num] = 1
            
            else:
                mp[num] += 1
        
    
        result = sorted(mp, key= mp.get, reverse = True)[:k]
        return result
        

