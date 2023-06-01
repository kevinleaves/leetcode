# https://leetcode.com/discuss/general-discussion/3570172/weekly-contest-347
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != "0":
            return num
        for i in range(len(num) - 1, -1, -1):
            if num[i] != "0":
                break
        return num[: i + 1]
