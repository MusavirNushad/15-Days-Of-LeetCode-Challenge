class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count = 0
        first_one_seen = False   # to ignore the first 1

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:   # nums[i] == 1
                if first_one_seen:               # for every 1 after the first one
                    if count < k:                # check spacing
                        return False
                first_one_seen = True            # mark first 1
                count = 0                        # reset count after 1

        return True

