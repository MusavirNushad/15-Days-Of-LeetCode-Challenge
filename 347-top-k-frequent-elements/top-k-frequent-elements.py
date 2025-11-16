class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        
        result = [item[0] for item in sorted_items[:k]]

        return result