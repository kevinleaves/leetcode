class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        first = strs[0]
        
        if len(first) == 0:
            return res

        for idx, c in enumerate(first):
            for i in range(1, len(strs)):
                if idx > len(strs[i]) -1:
                    return res
                if strs[i][idx] != c:
                    return res
            res += c
            
        return res
        

            