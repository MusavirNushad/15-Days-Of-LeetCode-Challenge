class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numsset = list(set(nums))
        sortlist = sorted(numsset)

        max_count = 1
        count = 1

        for i in range(1, len(sortlist)):
            if sortlist[i] == sortlist[i - 1] + 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1  

        return max_count
        