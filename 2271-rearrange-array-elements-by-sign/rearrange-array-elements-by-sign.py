class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        negarr = []
        posarr = []

        for num in nums:
            if num < 0:
                negarr.append(num)
            else:
                posarr.append(num)
        
        i = 0
        j = 0
        for k in range(len(nums)):
            if k%2 == 0:
                nums[k] = posarr[i]
                i+=1
            else:
                nums[k] = negarr[j]
                j+=1
        
        return nums