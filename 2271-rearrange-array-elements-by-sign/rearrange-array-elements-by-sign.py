class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # negarr = []
        # posarr = []

        # for num in nums:
        #     if num < 0:
        #         negarr.append(num)
        #     else:
        #         posarr.append(num)
        
        # i = 0
        # j = 0
        # for k in range(len(nums)):
        #     if k%2 == 0:
        #         nums[k] = posarr[i]
        #         i+=1
        #     else:
        #         nums[k] = negarr[j]
        #         j+=1
        
        # return nums

        pos = 0
        neg = 1
        n = len(nums)
        arr = [None]* n

        for num in nums:
            if num > 0:
                arr[pos] = num
                pos+=2
            else:
                arr[neg] = num
                neg+=2
        return arr