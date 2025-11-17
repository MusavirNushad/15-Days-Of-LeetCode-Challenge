class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count = 0
        first_one_seen = False  

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:  
                if first_one_seen:            
                    if count < k:                
                        return False
                first_one_seen = True          
                count = 0                        

        return True

