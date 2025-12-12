class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count0 = 0
        prod1 = 1
        for num in nums:
            if num == 0 and count0 <1:
                count0 += 1
                continue
            elif num == 0 and count0 == 1:
                count0+=1
                prod1= 0
                break
            else:
                prod1 *= num
        
        res = []
        if count0 > 1:
            for num in nums:
                res.append(0)
            return res
        
        for num2 in nums:
            if num2 == 0:
                res.append(prod1)
            elif count0 ==1 and num2 !=0:
                res.append(0)
            else:
                res.append(prod1//num2)
        
        return res