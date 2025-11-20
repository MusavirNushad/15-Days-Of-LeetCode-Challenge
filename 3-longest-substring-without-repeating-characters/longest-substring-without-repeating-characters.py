class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        


        if len(s) <= 1:
            return len(s)

        maxL = 0
        
        for i in range(len(s)):
            seen = set()
            l = 0

            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                l += 1
                maxL = max(maxL, l)

        return maxL
