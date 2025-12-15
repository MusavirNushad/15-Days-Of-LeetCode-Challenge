class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    
        # mp = defaultdict(list)

        # for s in strs:
        #     count = [0]*26
        #     for ch in s:
        #         count[ord(ch)- ord('a')] +=1

        #     key = tuple(count)

        #     mp[key].append(s)
        
        # return list(mp.values())

        f = {}

        for i in strs:
            t = "".join(sorted(i))
            if t in f:
                f[t].append(i)
            else:
                f[t] = [i]

        return list(f.values())