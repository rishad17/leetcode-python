class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""       
        p = 0
        x = ""
        while True:
            if p >= len(strs[0]):
                break           
            current_char = strs[0][p]           
            for s in strs:
                if p >= len(s) or s[p] != current_char:
                    return x 
            x += current_char
            p += 1
        return x
s=Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))