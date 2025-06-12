class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sum = 0
        flag = False
        for i in s[::-1]:
            if i == " ":
                if flag:
                    break
                continue
            else:
                sum += 1
                flag = True
        return sum
sol=Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))