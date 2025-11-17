class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        # count = 0
        # first_one_seen = False  

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count += 1
        #     else:  
        #         if first_one_seen:            
        #             if count < k:                
        #                 return False
        #         first_one_seen = True          
        #         count = 0                        

        # return True

        if k==0:
            return True
        
        prev = None

        for i, num in enumerate(nums):

            if num == 1:
                if prev is not None and i-prev <=k:
                    return False
                prev = i
        return True

