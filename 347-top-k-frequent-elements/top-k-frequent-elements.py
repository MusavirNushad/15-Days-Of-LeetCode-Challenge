import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}

        for num in nums:
            if num not in mp:
                mp[num] = 1
            
            else:
                mp[num] += 1
        
    
        result = heapq.nlargest(k, mp, key = mp.get)
        return result
        

