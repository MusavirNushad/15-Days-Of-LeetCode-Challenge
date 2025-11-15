class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        # count0 = 0
        # count1 = 0
        # count2 = 0

        # for num in nums:
        #  if num == 0:
        #     count0+=1
        #  elif num==1:
        #     count1+=1
        #  else:
        #     count2+=1
        
        # for i in range(len(nums)):
        #     if count0>0:
        #         nums[i] = 0
        #         count0-=1
        #     elif count1>0:
        #         nums[i] = 1
        #         count1-=1
        #     elif count2>0:
        #         nums[i] = 2
        #         count2-=1


        low, mid = 0,0
        high = len(nums)-1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1