class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}

        for n in s:
            freq[n] = freq.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(s)+1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        result = ""
        for i in range(len(buckets)-1,0, -1):
            for num in buckets[i]:
                result+= num*i
        
        return result