class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # n = len(nums)
        # orig = nums[:]            

        # for i in range(n):
        #     prevP = 1
        #     for p in range(i):       
        #         prevP *= orig[p]

        #     nextP = 1
        #     for j in range(i+1, n):
        #         nextP *= orig[j]

        #     nums[i] = prevP * nextP   

        # return nums

        n = len(nums)

        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
